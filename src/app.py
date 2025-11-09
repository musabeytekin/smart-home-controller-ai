import streamlit as st
from agents.supervisor.agent import supervisor_agent
from container import container

# Page configuration
st.set_page_config(
    page_title="Smart Home Controller",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS following modern design principles
st.markdown("""
    <style>
    /* Main container */
    .main {
        padding: 1rem 2rem;
    }
    
    /* Typography */
    h1 {
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    h2 {
        font-weight: 600;
        color: #1f2937;
        margin-top: 1.5rem;
    }
    
    /* Cards */
    .status-card {
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        border: 1px solid #e5e7eb;
        margin-bottom: 1rem;
    }
    
    .room-card {
        background: white;
        border-radius: 8px;
        padding: 1.25rem;
        margin-bottom: 1rem;
        border-left: 4px solid #3b82f6;
        box-shadow: 0 1px 2px rgba(0,0,0,0.05);
    }
    
    .room-card-off {
        border-left: 4px solid #6b7280;
    }
    
    /* Metrics */
    .metric-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0.75rem 0;
        border-bottom: 1px solid #f3f4f6;
    }
    
    .metric-row:last-child {
        border-bottom: none;
    }
    
    .metric-label {
        color: #6b7280;
        font-size: 0.875rem;
        font-weight: 500;
    }
    
    .metric-value {
        color: #111827;
        font-size: 1rem;
        font-weight: 600;
    }
    
    /* Status badges */
    .status-badge {
        display: inline-flex;
        align-items: center;
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        font-size: 0.875rem;
        font-weight: 500;
    }
    
    .badge-success {
        background-color: #d1fae5;
        color: #065f46;
    }
    
    .badge-warning {
        background-color: #fef3c7;
        color: #92400e;
    }
    
    .badge-danger {
        background-color: #fee2e2;
        color: #991b1b;
    }
    
    .badge-secondary {
        background-color: #f3f4f6;
        color: #374151;
    }
    
    /* Door list */
    .door-item {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0.75rem;
        background: #f9fafb;
        border-radius: 6px;
        margin: 0.5rem 0;
    }
    
    .door-name {
        font-weight: 500;
        color: #374151;
    }
    
    /* Input styling */
    .stChatInput {
        border-radius: 8px;
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #f9fafb;
    }
    
    /* Remove default streamlit padding */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
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
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask me to control your smart home..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Display assistant response
        with st.chat_message("assistant"):
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
    
    # Display Entry Door first
    with st.container(border=True):
        st.markdown(f"### 🚪 {house.entry_door.name}")
        st.caption("Main Entry to the House")
        
        lock_status = "❌ LOCKED" if house.entry_door.is_locked else "✅ UNLOCKED"
        st.metric("Status", lock_status)
    
    st.divider()
    
    # Display rooms in a grid
    cols_per_row = 2
    rooms = house.rooms
    
    for i in range(0, len(rooms), cols_per_row):
        cols = st.columns(cols_per_row)
        
        for j, col in enumerate(cols):
            if i + j < len(rooms):
                room = rooms[i + j]
                
                with col:
                    # Room card using Streamlit container
                    with st.container(border=True):
                        # Room name
                        st.markdown(f"### {room.name}")
                        
                        # Temperature and lights
                        col_a, col_b = st.columns(2)
                        with col_a:
                            st.metric("Temperature", f"{room.temperature}°C")
                        with col_b:
                            light_status_text = "On" if room.light_status else "Off"
                            light_icon = "💡" if room.light_status else "⚫"
                            st.metric("Lights", f"{light_icon} {light_status_text}")
                        
                        # Doors section
                        if room.doors:
                            st.markdown("---")
                            st.markdown(f"**Doors ({len(room.doors)})**")
                            
                            for door in room.doors:
                                lock_icon = "❌ LOCKED" if door.is_locked else "✅ UNLOCKED"
                                
                                # Door item
                                door_col1, door_col2 = st.columns([3, 1])
                                with door_col1:
                                    st.text(door.name)
                                with door_col2:
                                    st.text(f"{lock_icon}")

# Footer
st.divider()
st.caption(f"Smart Home Controller AI • {len(house.rooms)} rooms • {len(house.get_all_doors())} doors")
