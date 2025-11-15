import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Harley S. Reyes - Portfolio", page_icon="📘", layout="wide")

# --- GLOBAL STYLES ---
st.markdown(
    """
    <style>
    html, body, [class*="css"] {
        font-family: 'Segoe UI', sans-serif;
    }

    .about_css {
        color: #808080;
        font-size: 20px;
    }

    .project_css {
        color: #808080;
        font-size: 18px;
        font-style: italic;
    }

    .educ_school {
        font-size: 30px;
        font-style: italic;
        color: #444444;
    }

    .center-text {
        text-align: center;
    }

    .badge {
    display: inline-block;
    padding: 5px 10px;
    border-radius: 6px;
    background-color: #EEE; 
    color: #333;            
    margin-right: 6px;
    font-size: 14px;
    }

    [data-theme="dark"] .badge {
        background-color: #333; 
        color: #EEE;            
    }

    .hobbies {
        padding: 15px;
        text-align: center;
        border: 1px solid #e0e0e0;
        border-radius: 10px;
    }

    .contacts {
        padding: 15px; 
        border: 1px solid #e0e0e0; 
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- SIDEBAR ---
st.sidebar.image("DILAAB DIGITALS - Profile Photo.png", width=150)
st.sidebar.header("Harley S. Reyes")
st.sidebar.markdown("📍 Cebu, Philippines")
st.sidebar.markdown("📧 **harleyreyes879@gmail.com**")

st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to:", ["Homepage", "Portfolio", "Education"])

# --- HOMEPAGE ---
if page == "Homepage":

    st.markdown("<h1 class='center-text'>👋 Hi, I'm Harley S. Reyes</h1>", unsafe_allow_html=True)
    st.caption("Aspiring Software Developer | CS Student")

    st.image("DILAAB DIGITALS - Profile Photo.png", width=220)

    st.subheader("About Me")
    st.write("""
    I'm Harley S. Reyes, a 3rd year Bachelor of Science in Computer Science student at Cebu Institute of Technology – University.  
    I’m someone who never stops learning, exploring, and growing. My journey is shaped by curiosity, resilience, and a desire to make
    something meaningful from every experience.  
    """)

    st.write("---")
    st.subheader("Achievements")
    st.write("•  Overall Rank 7 in Computer Science Department of A.Y 23-24, FlexhibIT Awards (2024)")
    st.write("•  Academic Achiever, Parangal Awards (2025)")
    st.write("•  Academic Achiever, Parangal Awards (2024)")


    st.write("---")
    st.subheader("📞 Contacts")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="contacts">
            <h4>📧 Email</h4>
            <p><a href="mailto:harleyreyes879@gmail.com">harleyreyes879@gmail.com</a></p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="contacts">
            <h4>🔗 LinkedIn</h4>
            <p><a href="https://www.linkedin.com/in/harley-reyes-b0b830383/" target="_blank">Visit my LinkedIn Profile</a></p>
        </div>
        """, unsafe_allow_html=True)


    st.write("---")
    st.subheader("🎨 Hobbies & Interests")

    # 4 columns for hobbies
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="hobbies">
            <h3>🏃‍♂️</h3>
            <p><b>Running</b></p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="hobbies">
            <h3>📚</h3>
            <p><b>Reading</b></p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="hobbies">
            <h3>🎮</h3>
            <p><b>Playing League of Legends</b></p>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="hobbies">
            <h3>🏋️‍♂️</h3>
            <p><b>Gym / Working Out</b></p>
        </div>
        """, unsafe_allow_html=True)


# --- PORTFOLIO PAGE ---
elif page == "Portfolio":

    st.header("💼 My Projects")
    st.write(" ")

    # --- PROJECT 1 ---
    st.subheader("🎮 Finish Line - OOP2 Capstone")
    st.markdown("""
    <span class="badge">Java</span>
    <span class="badge">JavaFX</span>
    <span class="badge">SQL</span>
    """, unsafe_allow_html=True)

    with st.expander("📘 Project Description"):
        st.write("""
        Finish Line is a typing game developed as a capstone project by the Group SeraTeam from Cebu Institute of Technology – University (CIT-U).
        It aims to sharpen the player's typing proficiency while reinforcing key concepts across various Computer Science subjects.
        The gameplay is structured according to the official CIT-U College of Computer Studies curriculum, making it both educational and fun.
        """)
    st.markdown("[🔗 View Project](https://github.com/liya28/FinishLine)")

    st.write("---")

    # --- PROJECT 2 ---
    st.subheader("🛒 QuickCart - Mobile Development Project")
    st.markdown("""
    <span class="badge">Kotlin</span>
    <span class="badge">Android Development</span>
    """, unsafe_allow_html=True)

    with st.expander("📘 Project Description"):
        st.write("""
        QuickCart is a Kotlin-based Android app that streamlines grocery list creation and management.
        Designed for convenience and speed, it features an intuitive UI that helps users plan, organize, and shop efficiently.
        """)
    st.markdown("[🔗 View Project](https://github.com/muhadma/QuickCart)")

    st.write("---")

    # --- PROJECT 3 ---
    st.subheader("📚 AIOStubu - OOP1 Capstone")
    st.markdown("""
    <span class="badge">Java</span>
    <span class="badge">Desktop App</span>
    """, unsafe_allow_html=True)

    with st.expander("📘 Project Description"):
        st.write("""
        The All-In-One (AIO) Studdy Buddy (Stubu) is an offline-first productivity Windows desktop application 
        designed to equip students with essential learning tools such as reminders, notes, a timer, and more.
        """)
    st.markdown("[🔗 View Project](https://github.com/liya28/AIOStuBu)")

    st.write("---")

    # --- SKILLS ---
    st.header("⭐ Skills")
    st.write(" ")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("💻 Technical Skills")
        st.write("""
        - Web Design  
        - Programming  
        - Programming Languages:
            - C, C++, C#  
            - Java  
            - Kotlin  
            - Python  
        - Database Fundamentals
        - OOP & Data Structures
        """)

    with col2:
        st.subheader("🤝 Soft Skills")
        st.write("""
        - Communication  
        - Time Management  
        - Collaboration  
        - Adaptability  
        - Critical Thinking  
        """)

    
    st.write("---")
    # --- TECH STACK ---
    st.header("🧰 Tech Stack")
    st.write(" ")

    st.subheader("🔤 Programming Languages")
    st.markdown("""
    <span class="badge">Java</span>
    <span class="badge">Kotlin</span>
    <span class="badge">Python</span>
    <span class="badge">C</span>
    <span class="badge">C++</span>
    <span class="badge">C#</span>
    """, unsafe_allow_html=True)

    st.subheader("🌐 Web Development")
    st.markdown("""
    <span class="badge">HTML</span>
    <span class="badge">CSS</span>
    <span class="badge">JavaScript</span>
    <span class="badge">Streamlit</span>
    <span class="badge">Bootstrap</span>
    """, unsafe_allow_html=True)

    st.subheader("🗄️ Databases & Tools")
    st.markdown("""
    <span class="badge">MySQL</span>
    <span class="badge">SQLite</span>
    <span class="badge">Firebase</span>
    <span class="badge">Git</span>
    <span class="badge">GitHub</span>
    """, unsafe_allow_html=True)

    st.subheader("📱 Mobile & Desktop")
    st.markdown("""
    <span class="badge">Android Studio</span>
    <span class="badge">JavaFX</span>
    <span class="badge">SceneBuilder</span>
    """, unsafe_allow_html=True)

    st.write("---")
    st.subheader("📜 Certifications")
    st.write("• Codechum Java Object-Oriented Programming Certification Exam")
    st.write("• Codechum Java C Programming Certification Exam")


# --- EDUCATION PAGE ---
elif page == "Education":

    st.header("📚 Educational Background")

    st.subheader("🎓 Bachelor of Science in Computer Science")
    st.markdown('<p class="educ_school">Cebu Institute of Technology - University</p>', unsafe_allow_html=True)
    st.write("- Currently in 3rd year; coursework includes Automata Theory and Formal Languages," \
    " Information Management 2, Intelligent Systems 1, Quantitative Methods, and Applications." \
    " Development & Emerging Technologies")
    st.write("- Built strong foundations in computer literacy, programming, and graphic design through core courses and projects.")

    st.subheader("🎓 Senior High School (STEM Strand)")
    st.markdown('<p class="educ_school">Cebu Institute of Technology - University | Graduated July 2023</p>', unsafe_allow_html=True)
    st.write("- Consistent Honor Student, 12th Grade (SY 2022–2023) – 93% average")
    st.write("- Consistent Honor Student, 12th Grade (SY 2021–2022) – 92% average")

    st.subheader("🎓 Junior High School")
    st.markdown('<p class="educ_school">Cebu Institute of Technology - University | Graduated June 2021</p>', unsafe_allow_html=True)
    st.write("- Graduated With Honors – 96% average")

# --- FOOTER ---
st.markdown("---")
st.markdown("<div class='center-text'>Built with ❤️ using Streamlit</div>", unsafe_allow_html=True)