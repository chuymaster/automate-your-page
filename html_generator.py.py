#####-------------------------------------------------#####
#####Create HTML page for concepts studied in Lesson 2#####
#####-------------------------------------------------#####

###---------------------###
### Pre-defined Strings ###
###---------------------###

# Header String
HEADER_STRING = """<!DOCTYPE html>
<!-- This is an HTML comment -->
<html>
<head>
    <title>Udacity Introduction to Programming - Note for Project 2</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
<div class="whole">
    <div class="title">
        <h1>Important Concepts</h1>
    </div>"""
# Footer String
FOOTER_STRING = """</div>
</body>
</html>"""

# Concepts [Lesson Index, Header Index, Title, [Content Paragraph n, Concent Paragraph n+1,...]]
CONCEPT_LIST = [
[1,'1-1','Computer Language',["""Computer languages are different to Natural languages (E.g. English). Because natural languages have <em class="highlight">Ambiguity</em> and <em class="highlight">Verbosity</em> that will change the meanings of words based on the context. These 2 natures of natural languages can lead listeners to misunderstanding. If stupid computer listens to natural language, it will interpret wrongly and may launch a nuclear missile even though we order it to make a webpage."""]]
,[1,'1-2', 'Python',["""Python is a computer language. It has <em class="highlight">Grammar</em> where codes written in Python must match with. If the code has wrong grammar, a program will not run.""" ,"""Python has it's expressions. Every statement must be composed of <em class="highlight">Expression</em> + <em class="highlight">Operator</em> + <em class="highlight">Expression</em>. For example, 1 + 1 is ok but 1 1 is not."""]]
,[2,'2-1', 'Developer Tools',["""We can <em class="highlight">assign</em> a value to any variable. This way, a value will have a name therefore we can call it for later use. For example, we assign value 2 to a variable named 'i' by typing <em class="highlight">i = 2</em>. We can then print out 'i' by typing <em class="highlight">print i</em>."""]]
,[2,'2-2', 'String type value',["""A string can be defined by putting '' or "" in front and in back of any value. We can find if a string has any character inside by using <em class="highlight">string.find(string)</em> command. If there is, the number of position of that string will be returned."""]]
,[3,'3-1', 'Functions',["""Functions takes <em>Input</em>, do something and return <em>Output</em>. For example, a function Sum(a,b) takes 2 inputs, summarizes them and returns the summarized value as an output. We can define the above behavior of the function Sum by using <em class="highlight">def</em> keyword and return the processed result by <em class="highlight">return</em> keyword."""]]
,[3,'3-2', 'Avoiding Repetitions',["""Defining function to do something is similar to defining CSS stylesheet in project 1. We can use CSS in project 1 to apply the same style to contents scattered on html page. In the same way, we can call same function to produce results from many places in the program. Functions reduce repetition of coding same codes and make the program easy to maintain."""]]
,[4,'4-1', 'If',["""<em>If</em> splits program flow based on the evaluation result. For example, if 1 == 1 evaluates to <em class="highlight">True</em> so the code inside the if block is run. On the other hand, if 1 == 2 evaluates to <em class="highlight">False</em> therefore the code inside the if block is not run."""]]
,[4,'4-2', 'While',["""<em>While</em> instructs the program to execute the code inside its block in loop until the specified condition is met. We usually use while loop to process through all items inside the list.""","""However, beware that while loop is usually a cause of bug. Whether it is a <em class="highlight">forever loop</em> or loop through the object that does not exist."""]]
,[5,'5-1', 'List',["""List is a <em class="highlight">Structured Data</em>, data that can be break down. It is very useful to store a set of data. We can manipulate list in many ways.""", """Keywords: <em class="highlight">Mutation, Aliasing, Append, List + List, len(List), List.index(object), for object in List:</em>"""]]
,[6,'6-1', 'Solution',["""To solve any problem. We must first <em class="highlight">make sure we understand the problem</em> then...""","""1.DON'T PANIC""","""2.Know the inputs: know what is the set of valid inputs and how they are represented.""","""3.Know the Outputs: know the expected outputs and their formats.""","""4.Solve the problem: Work out examples by hand and develop incrementally."""]]
]

# Concepts Lesson List
LESSON_LIST = ['Lesson 1: Introduction to "Serious" Programming'
           ,'Lesson 2: Assign variable a value'
           ,'Lesson 3: Input -> Function -> Output'
           ,'Lesson 4: Control&Flow: If and While'
           ,'Lesson 5: Structured Data: List'
           ,'Lesson 6: How to solve the problem']
# Tab String
TAB_STRING = '    '

# Newline String
NEWLINE_STRING = """
"""

###---------###
### Methods ###
###---------###

# Table of Contents
def create_table_of_contents(concepts):
    toc = ''
    toc += NEWLINE_STRING + TAB_STRING + '<div class="toc">' + NEWLINE_STRING + TAB_STRING + '<ol>' + NEWLINE_STRING
    i = 0
    while i < len(concepts):
        concept = concepts[i]
        
	#Test if this concept is in the same header group as the previous. if not, create header link.
        if concepts[i][0] != concepts[i-1][0]:
            toc += TAB_STRING + '<li>' + NEWLINE_STRING
            toc += TAB_STRING + TAB_STRING + '<a href="#lesson-' + str(concept[0]) + '">' + LESSON_LIST[concept[0] - 1] + '</a>' + NEWLINE_STRING
            toc += TAB_STRING + TAB_STRING + '<ul>' + NEWLINE_STRING
            
	# Put in the concept title
        toc += TAB_STRING + TAB_STRING + TAB_STRING + '<li><a href="#lesson-' + concept[1] + '">' + concept[2] + '</a></li>' + NEWLINE_STRING
        
	#Test if the next concept is in the same header group as this one. If not, put the end </ul></li> tag.
        if i == len(concepts) - 1 or concepts[i][0] != concepts[i+1][0]:
            toc += TAB_STRING + TAB_STRING + '</ul>' + NEWLINE_STRING
            toc += TAB_STRING + '</li>' + NEWLINE_STRING
        i += 1
    toc += TAB_STRING + '</ol>' + NEWLINE_STRING + TAB_STRING + '</div>' + NEWLINE_STRING
    return toc

# Header
def create_html_header(concept):
    header = ''
    header += TAB_STRING + '<div class="header" id="lesson-' + str(concept[0]) + '">'
    header += LESSON_LIST[concept[0] - 1]
    header += '</div>' + NEWLINE_STRING
    return header

# Title
def create_html_title(concept):
    title = ''
    title += TAB_STRING + '<div class="subheader" id="lesson-' + str(concept[1]) + '">'
    title += concept[2]
    title += '</div>' + NEWLINE_STRING
    return title

# Content
def create_html_content(concept):
    content = ''
    content += TAB_STRING + '<div class="content">'
    for c in concept[3]:
        content += NEWLINE_STRING + TAB_STRING + TAB_STRING + '<p>'
        content += c
        content += '</p>'
    content += NEWLINE_STRING + TAB_STRING + '</div>' + NEWLINE_STRING
    return content

# Combine all HTMLs
def create_html(concepts):
    allhtml = ''
    allhtml += HEADER_STRING
    allhtml += create_table_of_contents(concepts)
    allhtml += TAB_STRING + '<div class="container">' + NEWLINE_STRING
    # Loop through all concepts in the list
    i = 0
    while i < len(concepts):
          allhtml += TAB_STRING + '<div class="contentbox">' + NEWLINE_STRING
          # Add lesson name for the first concept in each lesson
          if CONCEPT_LIST[i][0] != concepts[i-1][0]:
              allhtml += create_html_header(concepts[i])
          allhtml += create_html_title(concepts[i])
          allhtml += create_html_content(concepts[i])
          allhtml += TAB_STRING + '</div>' + NEWLINE_STRING
          i += 1
    allhtml += '</div>' + NEWLINE_STRING
    allhtml += FOOTER_STRING
    return allhtml

###--------------###
### Call Method! ###
###--------------###

print(create_html(CONCEPT_LIST))
