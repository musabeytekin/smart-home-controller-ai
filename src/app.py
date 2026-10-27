from html import escape

import streamlit as st
from agents.supervisor.agent import supervisor_agent
from container import container
from dotenv import load_dotenv

load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Smart Home Controller",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Shared card structure keeps room details aligned at every screen width.
def door_status_html(door):
    status = "Locked" if door.is_locked else "Unlocked"
    badge_class = "badge-locked" if door.is_locked else "badge-unlocked"
    return (
        '<li class="door-item">'
        f'<span class="door-name">{escape(door.name)}</span>'
        f'<span class="status-badge {badge_class}">{status}</span>'
        '</li>'
    )


def room_card_html(room):
    lighting = "💡 On" if room.light_status else "⚫ Off"
    doors = ''.join(door_status_html(door) for door in room.doors)
    door_list = f'<ul class="door-list">{doors}</ul>' if doors else '<p>No doors in this room.</p>'
    return (
        '<section class="room-card">'
        f'<h3>{escape(room.name)}</h3>'
        '<dl class="room-metrics">'
        f'<div><dt>Temperature</dt><dd>{escape(str(room.temperature))}°C</dd></div>'
        f'<div><dt>Lighting</dt><dd>{lighting}</dd></div>'
        '</dl>'
        '<div class="room-doors">'
        f'<h4>Doors ({len(room.doors)})</h4>{door_list}'
        '</div></section>'
    )


st.markdown("""
    <style>
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    .room-grid {
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 1.25rem;
    }

    .room-card {
        min-width: 0;
        padding: 1.25rem;
        border: 1px solid #80808055;
        border-radius: 12px;
        background: var(--secondary-background-color);
        color: var(--text-color);
        overflow-wrap: anywhere;
    }

    .room-card h3 {
        margin: 0 0 1rem;
        padding: 0;
        font-size: 1.25rem;
    }

    .room-metrics {
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 1rem;
        margin: 0;
    }

    .room-metrics dt {
        font-size: 0.875rem;
    }

    .room-metrics dd {
        margin: 0.25rem 0 0;
        font-size: 1.25rem;
        font-weight: 600;
    }

    .room-doors {
        margin-top: 1.25rem;
        padding-top: 1rem;
        border-top: 1px solid #80808055;
    }

    .room-doors h4 {
        margin: 0 0 0.5rem;
        padding: 0;
        font-size: 1rem;
    }

    .door-list {
        list-style: none;
        margin: 0;
        padding: 0;
    }

    .door-list .door-item {
        display: flex;
        flex-wrap: wrap;
        align-items: center;
        justify-content: space-between;
        gap: 0.5rem 1rem;
        margin: 0;
        padding: 0.625rem 0;
    }

    .door-name {
        flex: 1 1 10rem;
        min-width: 0;
        overflow-wrap: anywhere;
    }

    .status-badge {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        font-size: 0.875rem;
        font-weight: 600;
    }

    .badge-locked {
        background: #d1fae5;
        color: #065f46;
    }

    .badge-unlocked {
        background: #fef3c7;
        color: #92400e;
    }

    [data-testid="stChatMessage"] {
        min-width: 0;
        padding: 1rem;
        line-height: 1.6;
        overflow-wrap: anywhere;
    }

    @media (max-width: 700px) {
        .block-container {
            padding: 1rem;
        }

        .room-grid {
            grid-template-columns: minmax(0, 1fr);
            gap: 1rem;
        }

        .room-card {
            padding: 1rem;
        }
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Get house data
house = container.house

# Main header
col_header1, col_header2 = st.columns([3, 1])
with col_header1:
    st.title(f"🏠 {house.name}")
    st.caption("AI-powered smart home management system")
with col_header2:
    # Quick stats in header
    total_lights_on = sum(1 for room in house.rooms if room.light_status)
    total_rooms = len(house.rooms)
    if total_lights_on > 0:
        st.metric("Active Lights", f"{total_lights_on}/{total_rooms}", delta=None)

st.divider()

# Main content area
tab1, tab2 = st.tabs(["💬 Assistant", "🏘️ Rooms"])

# Tab 1: Chat Interface
with tab1:
    st.subheader("Chat with your Smart Home Assistant")
    
    st.caption("Manage lighting, temperature and door locks with a message.")

    conversation = st.container(height=400, border=True)
    with conversation:
        if not st.session_state.messages:
            st.caption('Try “Turn on the living room lights” or “Lock all doors”.')
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    # Keep the composer directly below the scrollable conversation.
    if prompt := st.chat_input("Ask me to control your smart home..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with conversation.chat_message("user"):
            st.markdown(prompt)
        
        # Display assistant response
        with conversation.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            
            # Process the agent's response
            try:
                with st.spinner("Processing your request..."):
                    final_response = None
                    
                    for step in supervisor_agent.stream(
                        {"messages": [{"role": "user", "content": prompt}]}
                    ):
                        for update in step.values():
                            for message in update.get("messages", []):
                                # Only capture AI messages (final responses), not tool messages
                                if hasattr(message, 'content') and message.content and hasattr(message, 'type') and message.type == 'ai':
                                    final_response = str(message.content)
                    
                    # Use the final AI response
                    if final_response:
                        full_response = final_response
                    else:
                        full_response = "✅ Command executed successfully!"
                    
                    message_placeholder.markdown(full_response)
                
            except Exception as e:
                full_response = f"❌ Error: {str(e)}"
                message_placeholder.markdown(full_response)
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": full_response})
        st.rerun()

# Tab 2: Room Details
with tab2:
    st.subheader("Room Overview")
    
    st.caption("View each room’s temperature, lighting and doors. Use the Assistant tab to make changes.")

    entry_door = (
        '<section class="room-card">'
        '<h3>🚪 Main entry</h3>'
        f'<ul class="door-list">{door_status_html(house.entry_door)}</ul>'
        '</section>'
    )
    st.markdown(entry_door, unsafe_allow_html=True)
    st.markdown("### Rooms")
    room_cards = ''.join(room_card_html(room) for room in house.rooms)
    st.markdown(f'<div class="room-grid">{room_cards}</div>', unsafe_allow_html=True)

# Footer
st.divider()
st.caption(f"Smart Home Controller AI • {len(house.rooms)} rooms • {len(house.get_all_doors())} doors")
