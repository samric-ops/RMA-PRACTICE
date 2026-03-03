import streamlit as st
from PIL import Image
import os
import datetime
import re

# --- APP CONFIG ---
st.set_page_config(page_title="Rapid Mathematics Assessment", page_icon="📝", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: #f0f2f6;
        border-radius: 5px 5px 0px 0px;
        gap: 1px;
    }
    .stTabs [aria-selected="true"] { background-color: #e0e2e6; font-weight: bold; }
    .stMultiSelect [data-baseweb="select"] { margin-bottom: 15px; }
    .figure-container {
        border: 2px solid #ddd;
        border-radius: 10px;
        padding: 20px;
        margin: 20px 0;
        background-color: #f9f9f9;
        text-align: center;
    }
    .figure-caption {
        font-weight: bold;
        margin-top: 10px;
        color: #666;
    }
    </style>
    """, unsafe_allow_html=True)

# --- FUNCTION TO DISPLAY FIGURES ---
def display_figure(figure_num, description, image_path=None):
    """Display figure with optional image"""
    st.markdown(f"**{description}**")
    
    if image_path and os.path.exists(image_path):
        image = Image.open(image_path)
        st.image(image, caption=f"Figure {figure_num}", use_container_width=True)
    else:
        st.warning(f"⚠️ **Figure {figure_num}** would be displayed here.")
        st.info(f"📌 **Instructions:** To display Figure {figure_num}, save the image as 'figure_{figure_num}.png' in the same folder as this app.")
        uploaded_file = st.file_uploader(f"Upload Figure {figure_num}", type=['png', 'jpg', 'jpeg'], key=f"upload_{figure_num}")
        if uploaded_file:
            st.image(uploaded_file, caption=f"Figure {figure_num} - {description}", use_container_width=True)

# --- SESSION STATE ---
if 'responses' not in st.session_state:
    st.session_state.responses = {}
if 'surname' not in st.session_state:
    st.session_state.surname = ""
if 'given_name' not in st.session_state:
    st.session_state.given_name = ""
if 'middle_name' not in st.session_state:
    st.session_state.middle_name = ""

# --- HEADER ---
st.title("Rapid Mathematics Assessment (Grades 7 - 10)")
st.write("---")

col1, col2, col3 = st.columns(3)
with col1:
    st.text_input("Surname", key="surname")
with col2:
    st.text_input("Given Name", key="given_name")
with col3:
    st.text_input("Middle Name", key="middle_name")
st.write("---")

st.markdown("""
## Assessment Instructions:

Your score on this test will help your teacher determine your readiness to learn the mathematics required at your grade level. You have **ninety (90) minutes** to complete this test.

Only the Questionnaire and Answer Sheet provided to you should be on your desk. Write all your solutions and answers, including any scratch work, directly on the Answer Sheet.

Before answering each question, double-check that the question numbers on your Answer Sheet match those on the Questionnaire to avoid misplaced answers. Please review your answers carefully before submitting your paper.

**i. For multiple-choice questions:**
Some multiple-choice questions may require selecting more than one answer. In such cases, write the letters of all your chosen options.

**ii. For short-answer questions:**
Provide clear and complete answers in the designated space provided on the Answer Sheet. Show all necessary calculations or explanations. You may write your explanations in English, Filipino, or Taglish.
""")

# --- SIDEBAR FORMULAS ---
with st.sidebar:
    st.header("📐 Formulas")
    st.markdown("""
    **Perimeter of a triangle:**  
    $P = a + b + c$
    
    **Area of a triangle:**  
    $A = \\frac{1}{2} \\times \\text{base} \\times \\text{height}$
    
    **Circumference of a circle:**  
    $C = 2\\pi r$
    
    **Area of a circle:**  
    $A = \\pi r^2$
    
    **Volume of a cylinder:**  
    $V = (\\text{area of the base}) \\times \\text{height}$
    """)
    
    st.divider()
    st.header("📁 Figure Files")
    st.markdown("""
    To display all figures, save these files in the app folder:
    - `figure_1.png` - Absences vs Academic Grade
    - `figure_2.png` - Monthly Family Income
    - `figure_3.png` - Number Line
    - `figure_4.png` - Cartesian Grid
    - `figure_5.png` - Tricycle Rental Cost
    - `figure_6.png` - Triangle PQR
    - `figure_7.png` - Dog House and Toy Storage
    - `figure_8.png` - Circular Pool (top view)
    - `figure_9.png` - Pool Depth (auxiliary view)
    - `figure_10.png` - Rolling Wheel
    """)

# --- MAIN TABS ---
tabs = st.tabs(["Items 1-11", "Items 12-22", "Items 23-33", "Items 34-47"])

# === TAB 1: Items 1-11 ===
with tabs[0]:
    st.subheader("Number Expressions")
    st.info("**Box 1:**")
    st.latex(r"2 \times 2 - 3 \times 1")
    st.latex(r"3 \times 3 - 4 \times 2")
    st.latex(r"4 \times 4 - 5 \times 3")
    st.latex(r"5 \times 5 - 6 \times 4")
    
    st.markdown("1. Your classmate said that each of the four expressions in Box 1 is equivalent to 1. Verify what your classmate said by showing your computation for the number expression $4 \\times 4 - 5 \\times 3$.")
    st.radio("Choose the correct result:", ["a) 1", "b) 2", "c) 0", "d) 3"], key="q1", index=None)
    
    st.markdown("2. What must be the next number expression to $5 \\times 5 - 6 \\times 4$ in Box 1?")
    st.radio("Choose the next expression:", ["a) 6 × 6 - 7 × 5", "b) 7 × 7 - 8 × 6", "c) 5 × 5 - 6 × 4", "d) 8 × 8 - 9 × 7"], key="q2", index=None)
    
    st.markdown("3. Which of the following algebraic expressions represents the set of number expressions in Box 1? **(Select all that apply)**")
    st.multiselect("Select your answer(s):", [
        "a. (n)(n) - (n + 3)(n + 1)",
        "b. (n)(n) - [(n + 1)(n - 1)]", 
        "c. (n - 1)(n - 1) - n(n - 2)",
        "d. n² - 3n(1)",
        "e. n² - n - 1"
    ], key="q3")
    
    st.markdown("4. Explain or show why you think you have chosen the correct algebraic expressions for the set of number expressions in Box 1.")
    st.radio("Choose the best explanation:", [
        "a) Because they all simplify to 1.",
        "b) Because they generate the same numbers.",
        "c) Because n represents the first number.",
        "d) Because they are algebraic expressions."
    ], key="q4", index=None)
    
    st.markdown("5. What does $n$ represent in your chosen expression in item 3?")
    st.radio("Choose the correct meaning:", [
        "a) The first number in each numerical expression (2,3,4,...)",
        "b) The second number",
        "c) The result",
        "d) The exponent"
    ], key="q5", index=None)
    
    st.divider()
    st.subheader("Powers and Rational Numbers")
    
    st.write("**Table 1**")
    st.markdown("""
| Exponential Form | Expanded Form | Power of 2 |
|---|---|---|
| 2² | 2 × 2 | 4 |
| 2³ | 2 × 2 × 2 | 8 |
| 2⁴ | 2 × 2 × 2 × 2 | 16 |
| 2⁵ | 2 × 2 × 2 × 2 × 2 | 32 |
    """)
    
    st.markdown("6. Show that 1024 is a power of 2. [Refer to Table 1]")
    st.radio("Which shows 1024 as a power of 2?", [
        "a) 1024 = 2¹⁰",
        "b) 1024 = 2⁹",
        "c) 1024 = 2⁸",
        "d) 1024 = 2⁷"
    ], key="q6", index=None)
    
    st.markdown("7. Write the exponential form of 1024.")
    st.radio("Exponential form:", [
        "a) 2¹⁰",
        "b) 2⁹",
        "c) 2⁸",
        "d) 2⁷"
    ], key="q7", index=None)
    
    st.markdown("8. Find a number that is a power of 2 that meets **BOTH** of these conditions:")
    st.markdown("* The number is a multiple of 16.  \n* The number is also more than 50 but less than 200.")
    st.radio("Choose the correct number:", [
        "a) 64",
        "b) 128",
        "c) 32",
        "d) 256"
    ], key="q8", index=None)
    
    st.markdown("9. Is there a number between 0.998 and 0.999? If YES, give one example. If NO, explain why you think so.")
    st.radio("Choose a correct example:", [
        "a) 0.9985",
        "b) 0.998",
        "c) 0.999",
        "d) 0.9991"
    ], key="q9", index=None)
    
    st.markdown("10. Show how you will subtract 0.998 from 0.999.")
    st.radio("What is the result?", [
        "a) 0.001",
        "b) 0.0001",
        "c) 0.01",
        "d) 0.1"
    ], key="q10", index=None)
    
    st.markdown("11. Is there a fraction that is greater than $\\frac{3}{4}$ but less than 1? If YES, give one example. If NO, explain why you think so.")
    st.radio("Choose a correct fraction:", [
        "a) 7/8",
        "b) 3/4",
        "c) 1/2",
        "d) 1"
    ], key="q11", index=None)

# === TAB 2: Items 12-22 ===
with tabs[1]:
    st.subheader("Data Interpretation")
    
    with st.container():
        st.markdown("### Figure 1: Relationship Between Absences and Academic Grade")
        st.markdown("*The graph shows the relationship between student absences and overall academic grade across all subjects in the Masipag section, a special class for arts and design, for two academic quarters. Each point on the graph represents an individual student.*")
        display_figure(1, "Absences vs Academic Grade", "figure_1.png")
    
    st.markdown("12. How many students had an overall academic grade below 84? [Refer to Figure 1]")
    st.radio("Number of students:", [
        "a) 5",
        "b) 4",
        "c) 6",
        "d) 7"
    ], key="q12", index=None)
    
    st.markdown("13. Explain why you think your answer in item 12 is correct based on the information shown in the graph in Figure 1.")
    st.radio("Best explanation:", [
        "a) There are five points with y‑coordinates below 84.",
        "b) The x‑coordinate of the point with y=84 is 5.",
        "c) There are four points below the line.",
        "d) The graph shows five absences."
    ], key="q13", index=None)
    
    st.markdown("14. Which of the following can be a correct interpretation of the data presented in the graph in Figure 1? **(Select all that apply)**")
    st.multiselect("Options for Item 14:", [
        "a. As the number of absences increases, the overall academic grade also increases.",
        "b. As the number of absences decreases, the overall academic grade increases.",
        "c. As the number of absences increases, the overall academic grade decreases.",
        "d. As the number of absences decreases, the overall academic grade also decreases."
    ], key="q14")
    
    st.divider()
    
    with st.container():
        st.markdown("### Figure 2: Monthly Family Income in Purok 1 and Purok 2")
        st.markdown("*Barangay San Mateo is planning to provide financial assistance for its two puroks. They surveyed the monthly family incomes in Purok 1 and Purok 2.*")
        display_figure(2, "Monthly Family Income", "figure_2.png")
    
    st.markdown("15. Based on the graph in Figure 2, which of the two puroks shows more diversity in monthly family income? Explain or justify your answer.")
    st.radio("Choose the correct statement:", [
        "a) Purok 1, because its income range is larger.",
        "b) Purok 2, because its incomes are more spread out.",
        "c) Purok 1, because it has more bars.",
        "d) Purok 2, because it has higher incomes."
    ], key="q15", index=None)
    
    st.markdown("16. The average monthly income of the families in Purok 1 and Purok 2 are equal. Should both purok be given the same amount of financial aid? What information in the graph in Figure 2 did you base your decision on?")
    st.radio("Choose the best decision and reason:", [
        "a) No, because Purok 1 has greater variability, so the average doesn't reflect most families.",
        "b) Yes, because they have the same average.",
        "c) No, because Purok 2 has more families.",
        "d) Yes, because both have same total income."
    ], key="q16", index=None)
    
    st.divider()
    st.subheader("Probability and Tables")
    st.write("**Table 2: Music and Sports Activities Participation**")
    st.markdown("*Malaya High School organized music and sports activities to celebrate the school's foundation day. Table 2 shows the participation of the Grade 7 students.*")
    
    st.markdown("""
| | Participated in sports | Did not participate in sports | Total |
|---|---|---|---|
| **Participated in music** | 18 | 31 | 49 |
| **Did not participate in music** | 42 | 19 | 61 |
| **Total** | 60 | 50 | 110 |
    """)
    
    st.markdown("17. How many students participated in the music activity?")
    st.radio("Number:", [
        "a) 49",
        "b) 60",
        "c) 18",
        "d) 31"
    ], key="q17", index=None)
    
    st.markdown("18. How many students did not participate in any of the two activities?")
    st.radio("Number:", [
        "a) 19",
        "b) 50",
        "c) 61",
        "d) 18"
    ], key="q18", index=None)
    
    st.markdown("19. What is the probability of selecting a student who participated in both music and sports activities?")
    st.radio("Probability:", [
        "a) 18/110",
        "b) 49/110",
        "c) 60/110",
        "d) 31/110"
    ], key="q19", index=None)
    
    st.markdown("20. Write a question that can be answered using the information in Table 2.")
    st.radio("Choose a question that can be answered:", [
        "a) How many students participated only in music?",
        "b) Why did students not participate?",
        "c) What is the average age of participants?",
        "d) How many students are in Grade 7?"
    ], key="q20", index=None)
    
    st.divider()
    st.subheader("Coordinates")
    
    with st.container():
        st.markdown("### Figure 3: Number Line")
        st.markdown("*A number describes the position of a point on a number line. The picture below is part of a number line.*")
        display_figure(3, "Number Line", "figure_3.png")
    
    st.markdown("21. What is the position of point \( F \) in Figure 3? **(Select all that apply)**")
    st.multiselect("Select your answer(s):", [
        "a. Point F is at -500",
        "b. Point F is at -400", 
        "c. Point F is at -300",
        "d. Point F is at -200",
        "e. Point F is at 50"
    ], key="q21")
    
    st.markdown("22. What is the position of point G in Figure 3?")
    st.radio("Position of G:", [
        "a) 0",
        "b) 100",
        "c) 200",
        "d) -100"
    ], key="q22", index=None)

# === TAB 3: Items 23-33 ===
with tabs[2]:
    st.subheader("Cartesian Plane")
    st.markdown("*An ordered pair of numbers describes the position of a point on a Cartesian plane. This position is called the coordinates of the point. The first number in the ordered pair is called the x-coordinate and the second number is called the y-coordinate.*")
    
    with st.container():
        st.markdown("### Figure 4: Cartesian Grid")
        display_figure(4, "Cartesian Grid", "figure_4.png")
    
    st.markdown("23. What are the coordinates of Point C in Figure 4?")
    st.radio("Coordinates:", [
        "a) (4,4)",
        "b) (3,4)",
        "c) (4,3)",
        "d) (5,5)"
    ], key="q23", index=None)
    
    st.markdown("24. A line is drawn passing through points B and C in Figure 4. Select two ordered pairs that represent the coordinates of points that are also in this line. **(Select exactly two)**")
    st.multiselect("Select points for Item 24:", [
        "a. (1, -1)", 
        "b. (1, -2)", 
        "c. (2, 3)", 
        "d. (3, 2)", 
        "e. (4, 7)", 
        "f. (5, 6)"
    ], key="q24", max_selections=2)
    
    st.markdown("25. Draw a line through points A and B in Figure 4. Which of the following ordered pairs represent all the points that are on this line? **(Select all that apply)**")
    st.multiselect("Options for Item 25:", [
        "a. (x, -2x)",
        "b. (x, -2x + 1)",
        "c. (x, -x)",
        "d. (x, -x + 1)",
        "e. (x, -x + 2)"
    ], key="q25")
    
    st.markdown("26. In Figure 4, connecting the points A, B and C will form a triangle, called triangle ABC. What is the area of triangle ABC? Show your method for getting the area.")
    st.radio("Area of triangle ABC:", [
        "a) 12 square units",
        "b) 10 square units",
        "c) 14 square units",
        "d) 8 square units"
    ], key="q26", index=None)
    
    st.markdown("27. A point represents position. Suppose in Figure 4, point A represents the position of your house, point B represents the position of your school and point C represents the position of the barangay hall. There is a straight road that you can take to the school and the barangay hall from your house. Which is the shorter walk from your house, going to the school or to the barangay hall?")
    st.radio("Shorter walk:", [
        "a) School",
        "b) Barangay hall",
        "c) They are equal",
        "d) Cannot determine"
    ], key="q27", index=None)
    
    st.markdown("28. Show or explain how you determined your answer in item 27.")
    st.radio("Best explanation:", [
        "a) Using distance formula, AB is shorter.",
        "b) By measuring with a ruler.",
        "c) Because the school is closer.",
        "d) Because the barangay hall is farther."
    ], key="q28", index=None)
    
    st.divider()
    st.subheader("Algebraic Reasoning")
    
    st.markdown("29. If $r$ is an integer, select all possible values that can be represented by $2r - 1$. **(Select all that apply)**")
    st.multiselect("Values for Item 29:", ["-5", "-27", "-82", "99", "46", "122"], key="q29")
    
    st.markdown("30. At a fruit stand, apples are priced at 3 for Php100. Which of the following expressions can be used to find the amount to be paid (cost) for any number ($n$) of apples? **(Select all that apply)**")
    st.multiselect("Options for Item 30:", [
        "a. cost = 100/3",
        "b. cost = 3n/100",
        "c. cost = 100n",
        "d. cost = 100n/3",
        "e. 3 : 100 = n : cost"
    ], key="q30")
    
    st.write("**Box 2:**")
    st.latex(r"17 + \_ = \_ + 3")
    st.markdown("*In Box 2 above, let a represent the number in the first blank space, and b represent the number in the second blank space.*")
    
    st.markdown("31. Write two possible values for $a$ and $b$ that will make the equation in Box 2 true.")
    st.radio("Which pair satisfies 17 + a = b + 3 ?", [
        "a) a=0, b=14",
        "b) a=1, b=15",
        "c) a=2, b=16",
        "d) All of the above"
    ], key="q31", index=None)
    
    st.markdown("32. Which statement is always true about $a$ and $b$? [Refer to Box 2] **(Select all that apply)**")
    st.multiselect("Options for Item 32:", [
        "a. a is greater than b.",
        "b. The sum of a and b, (a+b), is 20.",
        "c. The difference between b and a, (b-a), is 14.",
        "d. a and b can take any value."
    ], key="q32")
    
    st.markdown("33. Shown below is the solution to the given linear equation:")
    st.latex(r"5y - 8 = 14 - 3y \quad \text{---①}")
    st.latex(r"5y + 3y - 8 = 14 \quad \text{---②}")
    st.latex(r"8y - 8 = 14")
    st.latex(r"8y = 14 + 8")
    st.latex(r"8y = 22")
    st.latex(r"y = \frac{11}{4} \text{ or } 2.75")
    st.markdown("What reason can we use to transform equation ① into equation ②? **(Select all that apply)**")
    st.multiselect("Options for Item 33:", [
        "a. If we subtract 3y from both sides of equation ①, the equation will remain true.",
        "b. If we subtract 8 from both sides of equation ①, the equation will remain true.",
        "c. If we add 3y to both sides of equation ①, the equation will remain true.",
        "d. If we divide both sides of equation ① by 8, the equation will remain true."
    ], key="q33")

# === TAB 4: Items 34-47 ===
with tabs[3]:
    st.subheader("Equations and Graphs")
    st.markdown("*The cost of renting a tricycle per day is shown in the graph and formula below.*")
    
    with st.container():
        st.markdown("### Figure 5: Tricycle Rental Cost")
        st.markdown("Formula: $C = 250n + 200$")
        display_figure(5, "Tricycle Rental Cost Graph", "figure_5.png")
    
    st.markdown("34. How much does it cost to rent the tricycle for 5 days? [Refer to Figure 5]")
    st.radio("Cost for 5 days:", [
        "a) 1250",
        "b) 1450",
        "c) 1350",
        "d) 1550"
    ], key="q34", index=None)
    
    st.markdown("35. What does the number 250 in the formula represent? [Refer to Figure 5] **(Select all that apply)**")
    st.multiselect("Options for Item 35:", [
        "a. The daily cost of renting the tricycle.",
        "b. The number of days the tricycle is rented.",
        "c. The fixed cost of renting the tricycle.",
        "d. The total cost of renting for one day."
    ], key="q35")
    
    st.markdown("36. In Figure 5, what does the number 200 in the formula represent?")
    st.radio("200 represents:", [
        "a) Fixed cost",
        "b) Daily rate",
        "c) Total cost",
        "d) Number of days"
    ], key="q36", index=None)
    
    st.markdown("37. What aspect of the graph in Figure 5 represents the 200 in the formula? **(Select all that apply)**")
    st.multiselect("Options for Item 37:", [
        "a. x-intercept", 
        "b. y-intercept", 
        "c. slope", 
        "d. minimum point"
    ], key="q37")
    
    st.divider()
    st.subheader("Triangles")
    st.markdown("*Lines f, g, and h intersect at points P, Q and R, forming a triangle. The measures of the angles in degrees are represented by p, q and r.*")
    
    with st.container():
        st.markdown("### Figure 6: Triangle PQR")
        display_figure(6, "Triangle PQR", "figure_6.png")
    
    st.markdown("38. In Figure 6, if the measure of angle P is 30 degrees (that is, p = 30), which of the following are possible values for q and r? **Choose 2 that are correct** among the choices. Note that the triangle is not drawn to scale.")
    st.multiselect("Options for Item 38:", [
        "a. q = 10 and r = 140",
        "b. q = 10 and r = 130",
        "c. q = 110 and r = 30",
        "d. q = 100 and r = 80",
        "e. q = 100 and r = 50"
    ], key="q38", max_selections=2)
    
    st.markdown("39. In Figure 6, if the measure of angle R is 60 degrees (that is, $r = 60$) and the measure of the exterior angle at Q is 130, what is true about the values of p and q? **Choose at least one true statement** about p and q. NOTE: The exterior angle of a triangle forms a 180-degree angle with the adjacent interior angle.")
    st.multiselect("Options for Item 39:", [
        "a. The sum of p and q is 130.",
        "b. p and q can have several values.",
        "c. The value of p is 70 and the value of q is 50.",
        "d. The value of p is 50 and the value of q is 70.",
        "e. The value of r plus p is 130."
    ], key="q39")
    
    st.markdown("40. Which of the following statements about the properties of triangles will help determine the values of p and q in the preceding question? **Choose those that are applicable.** [Refer to Figure 6]")
    st.multiselect("Options for Item 40:", [
        "a. Each angle of an equilateral triangle is 60 degrees.",
        "b. In an isosceles triangle, the base angles are equal.",
        "c. The exterior angle and one of the interior angles adjacent to it form a linear pair.",
        "d. The measure of the exterior angle of a triangle is equal to the sum of the two remote interior angles.",
        "e. There are six exterior angles in any triangle.",
        "f. The sum of all the exterior angles of a triangle is 360 degrees."
    ], key="q40")
    
    st.divider()
    st.subheader("Proportionality")
    st.markdown("*Carlos built a house for his dog, Brownie. The lower part of the dog house serves as a sleeping area, while a small portion on top is used for toy storage. The base of the toy storage, which measures 25 centimeters, is parallel to the floor. The dog house is triangular with sides in the ratio of 3:3:2. The shortest side measures 1 meter.*")
    
    with st.container():
        st.markdown("### Figure 7: Dog House and Toy Storage")
        display_figure(7, "Dog House and Toy Storage", "figure_7.png")
    
    st.markdown("41. What are the lengths of the other two sides of the triangular dog house? [Refer to Figure 7] **(Select all that apply)**")
    st.multiselect("Options for Item 41:", [
        "a. The other two sides are 1.5 meters each.",
        "b. The other two sides are 2 meters and 3 meters.",
        "c. The other two sides are 3 meters each.",
        "d. The other two sides are 4 meters and 6 meters."
    ], key="q41")
    
    st.markdown("42. In Figure 7, are the sides of the triangular dog house proportional to the sides of the triangular toy storage? Show your solution or explain your answer.")
    st.radio("Are they proportional?", [
        "a) Yes, because the triangles are similar (parallel sides).",
        "b) No, because the sizes are different.",
        "c) Yes, because they are both triangles.",
        "d) No, because the ratios are not equal."
    ], key="q42", index=None)
    
    st.markdown("43. The base of the toy storage measures 25 centimeters. What are the lengths of its other two sides? [Refer to Figure 7] **(Select all that apply)**")
    st.multiselect("Options for Item 43:", [
        "a. The other two sides are 37.5 centimeters each.",
        "b. The other two sides measure 50 and 75 centimeters.",
        "c. The other two sides are 75 centimeters each.",
        "d. The other two sides measure 100 and 150 centimeters."
    ], key="q43")
    
    st.divider()
    st.subheader("Circles and Volumes")
    st.markdown("*A public park has a circular pool with a diameter of 10 meters. The park management decided to build a sidewalk around the pool to allow people to walk around it safely. The sidewalk has a uniform width of 1 meter all around the pool.*")
    
    with st.container():
        st.markdown("### Figure 8: Circular Pool (top view)")
        display_figure(8, "Circular Pool - Top View", "figure_8.png")
    
    with st.container():
        st.markdown("### Figure 9: Pool Depth (auxiliary view)")
        display_figure(9, "Pool Depth Diagram", "figure_9.png")
    
    st.markdown("44. What is the area of the sidewalk in square meters surrounding the pool? Show your solution. [Refer to Figure 8] Use $\\pi = 3.14$.")
    st.radio("Area of sidewalk:", [
        "a) 34.54 sq m",
        "b) 31.4 sq m",
        "c) 28.26 sq m",
        "d) 37.68 sq m"
    ], key="q44", index=None)
    
    # Item 45 (two-column layout)
    st.markdown("45. The park management decides to divide the pool into two equal parts. One part will be designated for adults and has a depth of 1.5 meters, while the other part will be designated for children and has a depth of 0.6 meters. Which of the following will give the total volume of water in the pool? [Refer to Figure 9] **(Select all that apply)**")
    st.caption("Select all correct answers:")

    for k in ["q45_a", "q45_b", "q45_c", "q45_d", "q45_e"]:
        if k not in st.session_state:
            st.session_state[k] = False

    def render_choice(letter_key: str, letter: str, latex_expr: str):
        row = st.columns([0.12, 0.58, 0.30])
        with row[0]:
            st.checkbox(letter, key=letter_key)
        with row[1]:
            st.latex(latex_expr)
        with row[2]:
            st.write("cubic meters")

    left_col, right_col = st.columns(2)
    with left_col:
        render_choice("q45_a", "a.", r"10\pi(2.1)")
        render_choice("q45_b", "b.", r"25\pi(2.1)")
        render_choice("q45_c", "c.", r"\frac{10\pi(2.1)}{2}")
    with right_col:
        render_choice("q45_d", "d.", r"\frac{25\pi(2.1)}{2}")
        render_choice("q45_e", "e.", r"\frac{100\pi(2.1)}{2}")

    selected_q45 = []
    if st.session_state["q45_a"]: selected_q45.append("a. 10π(2.1) cubic meters")
    if st.session_state["q45_b"]: selected_q45.append("b. 25π(2.1) cubic meters")
    if st.session_state["q45_c"]: selected_q45.append("c. (10π(2.1))/2 cubic meters")
    if st.session_state["q45_d"]: selected_q45.append("d. (25π(2.1))/2 cubic meters")
    if st.session_state["q45_e"]: selected_q45.append("e. (100π(2.1))/2 cubic meters")
    st.session_state["q45"] = selected_q45

    st.divider()
    st.subheader("Rotation and Distance")
    st.markdown("*A wheel with a diameter of 60 cm is rolled along a straight path.*")
    
    with st.container():
        st.markdown("### Figure 10: Rolling Wheel")
        display_figure(10, "Rolling Wheel", "figure_10.png")
    
    st.markdown("46. The wheel in Figure 10 is rolled exactly 5 times. Show how you can compute the distance travelled by the wheel.")
    st.radio("Distance travelled:", [
        "a) 942 cm",
        "b) 300π cm",
        "c) 188.4 cm",
        "d) Both a and b are correct"
    ], key="q46", index=None)
    
    st.markdown("47. How many degrees did the wheel's pin rotate after 5 rolls? [Refer to Figure 10]")
    st.radio("Degrees rotated:", [
        "a) 1800°",
        "b) 360°",
        "c) 720°",
        "d) 900°"
    ], key="q47", index=None)

# =============================================================================
# SCORING ENGINE (based on official RMA scoring guide)
# =============================================================================

def score_item(item_key, ans, all_answers):
    """Return points earned for a given item (0,1,2,3)."""
    # Helper to check if answer is empty
    if ans is None or ans == "" or (isinstance(ans, list) and len(ans)==0):
        return 0

    # Item 1
    if item_key == "q1":
        return 2 if ans == "a) 1" else 0

    # Item 2
    if item_key == "q2":
        return 1 if ans == "a) 6 × 6 - 7 × 5" else 0

    # Item 3 (multiselect)
    if item_key == "q3":
        correct_set = {"b. (n)(n) - [(n + 1)(n - 1)]", "c. (n - 1)(n - 1) - n(n - 2)"}
        user_set = set(ans) if isinstance(ans, list) else set()
        if user_set == correct_set:
            return 2
        if user_set == {"b. (n)(n) - [(n + 1)(n - 1)]"} or user_set == {"c. (n - 1)(n - 1) - n(n - 2)"}:
            return 1
        return 0

    # Item 4
    if item_key == "q4":
        return 2 if ans == "a) Because they all simplify to 1." else 0

    # Item 5
    if item_key == "q5":
        return 1 if ans == "a) The first number in each numerical expression (2,3,4,...)" else 0

    # Item 6
    if item_key == "q6":
        return 2 if ans == "a) 1024 = 2¹⁰" else 0

    # Item 7
    if item_key == "q7":
        return 1 if ans == "a) 2¹⁰" else 0

    # Item 8 (two correct options)
    if item_key == "q8":
        return 1 if ans in ["a) 64", "b) 128"] else 0

    # Item 9
    if item_key == "q9":
        return 1 if ans == "a) 0.9985" else 0

    # Item 10
    if item_key == "q10":
        return 2 if ans == "a) 0.001" else 0

    # Item 11
    if item_key == "q11":
        return 2 if ans == "a) 7/8" else 0

    # Item 12
    if item_key == "q12":
        return 1 if ans == "a) 5" else 0

    # Item 13
    if item_key == "q13":
        return 1 if ans == "a) There are five points with y‑coordinates below 84." else 0

    # Item 14 (multiselect)
    if item_key == "q14":
        correct_set = {"b. As the number of absences decreases, the overall academic grade increases.",
                       "c. As the number of absences increases, the overall academic grade decreases."}
        user_set = set(ans) if isinstance(ans, list) else set()
        if user_set == correct_set:
            return 2
        if user_set == {"b. As the number of absences decreases, the overall academic grade increases."} or \
           user_set == {"c. As the number of absences increases, the overall academic grade decreases."}:
            return 1
        return 0

    # Item 15
    if item_key == "q15":
        return 2 if ans == "a) Purok 1, because its income range is larger." else 0

    # Item 16
    if item_key == "q16":
        return 2 if ans == "a) No, because Purok 1 has greater variability, so the average doesn't reflect most families." else 0

    # Item 17
    if item_key == "q17":
        return 1 if ans == "a) 49" else 0

    # Item 18
    if item_key == "q18":
        return 1 if ans == "a) 19" else 0

    # Item 19
    if item_key == "q19":
        return 1 if ans == "a) 18/110" else 0

    # Item 20
    if item_key == "q20":
        return 1 if ans == "a) How many students participated only in music?" else 0

    # Item 21 (multiselect)
    if item_key == "q21":
        user_set = set(ans) if isinstance(ans, list) else set()
        correct = {"c. Point F is at -300"}
        return 1 if user_set == correct else 0

    # Item 22
    if item_key == "q22":
        return 1 if ans == "a) 0" else 0

    # Item 23
    if item_key == "q23":
        return 1 if ans == "a) (4,4)" else 0

    # Item 24 (multiselect)
    if item_key == "q24":
        user_set = set(ans) if isinstance(ans, list) else set()
        correct_options = {"b. (1, -2)", "d. (3, 2)", "f. (5, 6)"}
        if len(user_set) == 2 and user_set.issubset(correct_options):
            return 2
        if len(user_set) == 1 and user_set.issubset(correct_options):
            return 1
        return 0

    # Item 25 (multiselect)
    if item_key == "q25":
        user_set = set(ans) if isinstance(ans, list) else set()
        correct = {"e. (x, -x + 2)"}
        return 1 if user_set == correct else 0

    # Item 26
    if item_key == "q26":
        return 2 if ans == "a) 12 square units" else 0

    # Item 27
    if item_key == "q27":
        return 1 if ans == "a) School" else 0

    # Item 28
    if item_key == "q28":
        return 2 if ans == "a) Using distance formula, AB is shorter." else 0

    # Item 29 (multiselect)
    if item_key == "q29":
        user_set = set(ans) if isinstance(ans, list) else set()
        correct = {"-5", "-27", "99"}
        if user_set == correct:
            return 3
        if len(user_set) == 2 and user_set.issubset(correct):
            return 2
        if len(user_set) == 1 and user_set.issubset(correct):
            return 1
        return 0

    # Item 30 (multiselect)
    if item_key == "q30":
        user_set = set(ans) if isinstance(ans, list) else set()
        correct = {"d. cost = 100n/3", "e. 3 : 100 = n : cost"}
        if user_set == correct:
            return 2
        if user_set == {"d. cost = 100n/3"} or user_set == {"e. 3 : 100 = n : cost"}:
            return 1
        return 0

    # Item 31
    if item_key == "q31":
        return 2 if ans == "d) All of the above" else 0

    # Item 32 (multiselect)
    if item_key == "q32":
        user_set = set(ans) if isinstance(ans, list) else set()
        correct = {"c. The difference between b and a, (b-a), is 14."}
        return 1 if user_set == correct else 0

    # Item 33 (multiselect)
    if item_key == "q33":
        user_set = set(ans) if isinstance(ans, list) else set()
        correct = {"c. If we add 3y to both sides of equation ①, the equation will remain true."}
        return 1 if user_set == correct else 0

    # Item 34
    if item_key == "q34":
        return 1 if ans == "b) 1450" else 0

    # Item 35 (multiselect)
    if item_key == "q35":
        user_set = set(ans) if isinstance(ans, list) else set()
        correct = {"a. The daily cost of renting the tricycle."}
        return 1 if user_set == correct else 0

    # Item 36
    if item_key == "q36":
        return 1 if ans == "a) Fixed cost" else 0

    # Item 37 (multiselect)
    if item_key == "q37":
        user_set = set(ans) if isinstance(ans, list) else set()
        correct = {"b. y-intercept"}
        return 1 if user_set == correct else 0

    # Item 38 (multiselect)
    if item_key == "q38":
        user_set = set(ans) if isinstance(ans, list) else set()
        correct = {"a. q = 10 and r = 140", "e. q = 100 and r = 50"}
        if user_set == correct:
            return 2
        if user_set == {"a. q = 10 and r = 140"} or user_set == {"e. q = 100 and r = 50"}:
            return 1
        return 0

    # Item 39 (multiselect)
    if item_key == "q39":
        user_set = set(ans) if isinstance(ans, list) else set()
        correct = {"c. The value of p is 70 and the value of q is 50.",
                   "e. The value of r plus p is 130."}
        if user_set == correct:
            return 2
        if user_set == {"c. The value of p is 70 and the value of q is 50."} or \
           user_set == {"e. The value of r plus p is 130."}:
            return 1
        return 0

    # Item 40 (multiselect)
    if item_key == "q40":
        user_set = set(ans) if isinstance(ans, list) else set()
        correct = {"c. The exterior angle and one of the interior angles adjacent to it form a linear pair.",
                   "d. The measure of the exterior angle of a triangle is equal to the sum of the two remote interior angles."}
        if user_set == correct:
            return 2
        if user_set == {"c. The exterior angle and one of the interior angles adjacent to it form a linear pair."} or \
           user_set == {"d. The measure of the exterior angle of a triangle is equal to the sum of the two remote interior angles."}:
            return 1
        return 0

    # Item 41 (multiselect)
    if item_key == "q41":
        user_set = set(ans) if isinstance(ans, list) else set()
        correct = {"a. The other two sides are 1.5 meters each."}
        return 1 if user_set == correct else 0

    # Item 42
    if item_key == "q42":
        return 2 if ans == "a) Yes, because the triangles are similar (parallel sides)." else 0

    # Item 43 (multiselect)
    if item_key == "q43":
        user_set = set(ans) if isinstance(ans, list) else set()
        correct = {"a. The other two sides are 37.5 centimeters each."}
        return 1 if user_set == correct else 0

    # Item 44
    if item_key == "q44":
        return 3 if ans == "a) 34.54 sq m" else 0

    # Item 45 (list from checkboxes)
    if item_key == "q45":
        user_set = set(ans) if isinstance(ans, list) else set()
        correct = {"d. (25π(2.1))/2 cubic meters"}
        return 1 if user_set == correct else 0

    # Item 46
    if item_key == "q46":
        return 2 if ans == "d) Both a and b are correct" else 0

    # Item 47
    if item_key == "q47":
        return 2 if ans == "a) 1800°" else 0

    return 0

def compute_all_scores():
    """Return dict of item->score and total score."""
    scores = {}
    total = 0
    for i in range(1, 48):
        key = f"q{i}"
        ans = st.session_state.get(key, None)
        if key == "q45":
            ans = st.session_state.get("q45", [])
        score = score_item(key, ans, st.session_state)
        scores[key] = score
        total += score
    return scores, total

# --- FOOTER: SUBMISSION AND RESULTS ---
st.divider()

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("✅ Complete Assessment", use_container_width=True):
        if not st.session_state.surname or not st.session_state.given_name:
            st.warning("Please enter your surname and given name before submitting.")
        else:
            st.balloons()
            st.success("Responses submitted successfully!")
            
            scores, total_score = compute_all_scores()
            max_possible = 71  # from scoring guide sum
            
            st.subheader("📋 Assessment Summary")
            st.write(f"**Student:** {st.session_state.surname}, {st.session_state.given_name} {st.session_state.middle_name}")
            st.write(f"**Total Score:** {total_score} / {max_possible}  ({total_score/max_possible*100:.1f}%)")
            
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"RMA_{st.session_state.surname}_{st.session_state.given_name}_{timestamp}.txt"
            lines = []
            lines.append("RAPID MATHEMATICS ASSESSMENT RESULTS")
            lines.append("="*50)
            lines.append(f"Student: {st.session_state.surname}, {st.session_state.given_name} {st.session_state.middle_name}")
            lines.append(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")
            lines.append(f"Total Score: {total_score} / {max_possible} ({total_score/max_possible*100:.1f}%)")
            lines.append("="*50)
            lines.append("\nDETAILED SCORES:")
            for i in range(1,48):
                key = f"q{i}"
                score = scores.get(key,0)
                lines.append(f"{key.upper()}: {score}")
            lines.append("="*50)
            content = "\n".join(lines)
            
            st.download_button(
                label="📥 Download Summary as Text File",
                data=content,
                file_name=filename,
                mime="text/plain"
            )
            
            with st.expander("View Detailed Scores"):
                for i in range(1,48):
                    key = f"q{i}"
                    st.write(f"**{key.upper()}:** {scores.get(key,0)}")
