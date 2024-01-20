import streamlit as st

# Set Streamlit configurations if needed
st.set_page_config(page_title="Portofolio Web App", layout="wide")

# Adding CSS styles
st.markdown(
    ''' 
    <style>
    div[data-testid="stHorizontalBlock"] > div:first-of-type {
        background-color: #577891;
        font-size: 8px;
        padding: 10px; /* Menambahkan padding untuk memberi ruang pada elemen */
    }

    .container {
        margin-top: 10px; /* Memberi ruang antara elemen container */
    }
    </style>
    ''',
    unsafe_allow_html=True
)

# Creating layout columns
col_1, col_2 = st.columns([1, 4])

# Column 1
with col_1:

    # Photo
    with st.container():
        st.image("foto_pribadi.jpg", use_column_width=True)    
    with st.container(height=20, border=False):
        pass


    # Biodata
    with st.container():
        original_title = '<p style="font-family: Courier; color: white; font-size: 20px; font-weight: Bold;">Biodata</p>'
        st.markdown(original_title, unsafe_allow_html=True)
        st.markdown('<p style="font-family: Courier; color: white; font-size: 16px;">Kota Asal: Medan</p>', unsafe_allow_html=True)
        st.markdown('<p style="font-family: Courier; color: white; font-size: 16px;">Tanggal Lahir: 14 Juni 2003</p>', unsafe_allow_html=True)
        st.markdown('<p style="font-family: Courier; color: white; font-size: 16px;">Alamat: Kyai Syahdan, Jakarta Barat</p>', unsafe_allow_html=True)
    
    with st.container(height=5, border=False):
        pass
   
#    kemampuan bahasa
    with st.container():
        original_title = '<p style="font-family: Courier; color: white; font-size: 20px; font-weight: Bold;">Kemampuan Bahasa</p>'
        st.markdown(original_title, unsafe_allow_html=True)
        st.markdown('<p style="font-family: Courier; color: white; font-size: 16px;">Bahasa Indonesia: Fasih</p>', unsafe_allow_html=True)
        st.markdown('<p style="font-family: Courier; color: white; font-size: 16px;">Bahasa Inggris: Menengah</p>', unsafe_allow_html=True)
       
    with st.container(height=5, border=False):
        pass  # Tambahkan container kosong jika diperlukan untuk memberikan ruang

    with st.container():
        original_title = '<p style="font-family: Courier; color: white; font-size: 20px; font-weight: Bold;">Skills</p>'
        st.markdown(original_title, unsafe_allow_html=True)
        teks = '''
        Python, SQL, Tableau, Figma, 
        Visual Faradigm 17.0, Microsoft Office
        '''
        st.markdown(f'<p style="font-family: Courier; color: white; font-size: 14px;">{teks}</p>', unsafe_allow_html=True)
       
    with st.container(height=5, border=False):
        pass 

    with st.container():
        original_title = '<p style="font-family: Courier; color: white; font-size: 20px; font-weight: Bold;">Certificate</p>'
        st.markdown(original_title, unsafe_allow_html=True)
        teks = '''
        Python Fundamental for Data Science by DQLab (2023), 
        Data Wrangling Python by DQlab (2023), 
        Belajar Dasar Structured uery Language (SQL) by dicoding (2023)
        '''
        st.markdown(f'<p style="font-family: Courier; color: white; font-size: 14px;">{teks}</p>', unsafe_allow_html=True)
       
    with st.container(height=30, border=False):
        pass 

# Column 2
with col_2:
    # perkenalan
    with st.container():
        original_title = '<p style="font-family: Courier; color: Black; font-size: 30px; font-weight: Bold;">Vieri Aska Juneio Sembiring</p>'
        st.markdown(original_title, unsafe_allow_html=True)
        with st.container(height=5, border=False):
            pass
        # Summary

    with st.container():   
        original_title = '<p style="font-family: Courier; color: black; font-size: 20px; font-weight: Bold;">Portofolio</p>'
        st.markdown(original_title, unsafe_allow_html=True)

        link = 'https://www.notion.so/vieriaska/Vieri-Aska-Juneio-Sembiring-s-Portfolio-f7d0331b558b4e5fa4a9f6e45131fcf2'
        link_text = "Vieri Aska Juneio Sembiring's Portofolio"
        st.markdown(f'<a href="{link}" target="_blank" style="font-family: Courier; color: blue; font-size: 14px;">{link_text}</a>', unsafe_allow_html=True)

    with st.container(height=5, border=False):
        pass

    with st.container():   
        original_title = '<p style="font-family: Courier; color: black; font-size: 20px; font-weight: Bold;">SUMMARY</p>'
        st.markdown(original_title, unsafe_allow_html=True)
        teks = '''
        An active fifth-semester undergraduate student of Information Systems at Bina Nusantara University with a strong interest
        in Data Analysis, Business Analysis, and UI/UX Design. Alongside my studies, I have gained experience as an Volunteer
        at PO Peduli BINUS and School of Information Systems Company Visit. I also had the opportunity to take a part in an
        member at Information System Case Study Club. All my experience taught me how to develop a strong work ethic, attention
        to detail, and the ability to thrive in a fast-paced and dynamic work environment.
            '''
        st.markdown(f'<p style="font-family: Courier; color: black; font-size: 14px;">{teks}</p>', unsafe_allow_html=True)
        with st.container(height=5, border=False):
            pass

            # Education
    with st.container():   
        original_title = '<p style="font-family: Courier; color: black; font-size: 20px; font-weight: Bold;">EDUCATION</p>'
        st.markdown(original_title, unsafe_allow_html=True)
        st.markdown(f'<p style="font-family: Courier; color: black; font-size: 16px;font-weight: Bold;">Bina Nusantara University (September 2021 - Present)</p>', unsafe_allow_html=True)
        teks = '''
        Undergraduate Information Systems - GPA: 3.83 out of 4.00
        '''
        st.markdown(f'<p style="font-family: Courier; color: black; font-size: 14px;">{teks}</p>', unsafe_allow_html=True)
        with st.container(height=5, border=False):
            pass
        
        # organisasi
    with st.container():   
        original_title = '<p style="font-family: Courier; color: black; font-size: 20px; font-weight: Bold;">ORGANIZATION EXPERIENCE</p>'
        st.markdown(original_title, unsafe_allow_html=True)
        st.markdown(f'<p style="font-family: Courier; color: black; font-size: 16px;font-weight: Bold;"> Information System Case Study Club - Jakarta Member (March 2023 - January 2024) </p>', unsafe_allow_html=True) 
        teks = '''
        • Collect and analyze data for research to solve cases • Producing posters and infographics • Producing UI/UX design work • Develop analytical thinking and communication skills • Preparation for participating in national or international competitions
        '''
        st.markdown(f'<p style="font-family: Courier; color: black; font-size: 14px;">{teks}</p>', unsafe_allow_html=True)
        with st.container(height=5, border=False):
            pass

        # volunteer
    with st.container():   
        original_title = '<p style="font-family: Courier; color: black; font-size: 20px; font-weight: Bold;">VOLUNTEER EXPERIENCE</p>'
        st.markdown(original_title, unsafe_allow_html=True)
        st.markdown(f'<p style="font-family: Courier; color: black; font-size: 16px;font-weight: Bold;">PO Peduli BINUS - Jakarta Volunteer (2023)</p>', unsafe_allow_html=True)
        teks = '''
        • Accompanying orphanage children and providing instructions in coloring and sharing activities to make the event a success
        • Assisting the committee in disseminating the outcomes of event activities via social media
        '''
        st.markdown(f'<p style="font-family: Courier; color: black; font-size: 14px;">{teks}</p>', unsafe_allow_html=True)
        st.markdown(f'<p style="font-family: Courier; color: black; font-size: 16px;font-weight: Bold;">School of Information Systems Company Visit - Jakarta Volunteer (2023)</p>', unsafe_allow_html=True)
        teks1= '''
        • Assisting Artisa Tangerang High School students in their company visit to BCA Landmark Pluit activities
        • Telling about experiences while participating in lectures, competitions, and club activities at the School of Information Systems
        '''
        st.markdown(f'<p style="font-family: Courier; color: black; font-size: 14px;">{teks1}</p>', unsafe_allow_html=True)


           


