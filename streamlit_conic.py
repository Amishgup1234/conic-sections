import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Title of the webpage will be Passion
st.title('Passion')

# Create a selectbox for the menu
shape = st.selectbox('Choose a shape', ['Circle', 'Ellipse', 'Hyperbola', 'Parabola'])

# Define the range of values for the variables
x_vals = np.linspace(-5, 5, 100)

if shape == 'Circle':
    # Circle equation (x-a)^2 + (y-b)^2 = r^2
    a = st.number_input("Enter the x-coordinate for the center of the circle", min_value=-10.0, value=0.0)
    b = st.number_input("Enter the y-coordinate for the center of the circle", min_value=-10.0, value=0.0)
    r = st.number_input("Enter the radius for the circle", min_value=0.0, value=1.0)
    theta = np.linspace(0, 2*np.pi, 100)
    x_vals = a + r * np.cos(theta)
    y_vals = b + r * np.sin(theta)
    plt.plot(x_vals, y_vals, color='b')

elif shape == 'Ellipse':
    # Ellipse equations (x^2/a^2) + (y^2/b^2) = 1 and (x^2/b^2) + (y^2/a^2) = 1
    orientation = st.selectbox("Choose the orientation of the ellipse", ['Horizontal (x^2/a^2 + y^2/b^2 = 1)', 'Vertical (x^2/b^2 + y^2/a^2 = 1)'])
    a = st.number_input("Enter the value for 'a' in the ellipse equation", min_value=0.0, value=1.0)
    b = st.number_input("Enter the value for 'b' in the ellipse equation", min_value=0.0, value=1.0)
    theta = np.linspace(0, 2*np.pi, 100)
    if orientation == 'Horizontal (x^2/a^2 + y^2/b^2 = 1)':
        x_vals = a * np.cos(theta)
        y_vals = b * np.sin(theta)
    elif orientation == 'Vertical (x^2/b^2 + y^2/a^2 = 1)':
        x_vals = b * np.cos(theta)
        y_vals = a * np.sin(theta)
    plt.plot(x_vals, y_vals, color='g')

elif shape == 'Hyperbola':
    # Hyperbola equations (x^2/a^2) - (y^2/b^2) = 1 and (x^2/b^2) - (y^2/a^2) = 1
    orientation = st.selectbox("Choose the orientation of the hyperbola", ['Horizontal (x^2/a^2 - y^2/b^2 = 1)', 'Vertical (x^2/b^2 - y^2/a^2 = 1)'])
    a = st.number_input("Enter the value for 'a' in the hyperbola equation", min_value=0.0, value=1.0)
    b = st.number_input("Enter the value for 'b' in the hyperbola equation", min_value=0.0, value=1.0)
    theta = np.linspace(-np.pi/2, np.pi/2, 400)
    if orientation == 'Horizontal (x^2/a^2 - y^2/b^2 = 1)':
        x_vals = a * np.cosh(theta)
        y_vals = b * np.sinh(theta)
        plt.plot(x_vals, y_vals, color='y')
        plt.plot(-x_vals, y_vals, color='y')  # Plot the left branch of the hyperbola
    elif orientation == 'Vertical (x^2/b^2 - y^2/a^2 = 1)':
        x_vals = b * np.sinh(theta)
        y_vals = a * np.cosh(theta)
        plt.plot(x_vals, y_vals, color='y')
        plt.plot(x_vals, -y_vals, color='y')  # Plot the bottom branch of the hyperbola

elif shape == 'Parabola':
    # Parabola equations y^2 = 4ax, y^2 = -4ax, x^2 = 4ay, x^2 = -4ay
    orientation = st.selectbox("Choose the orientation of the parabola", ['Right (y^2 = 4ax)', 'Left (y^2 = -4ax)', 'Up (x^2 = 4ay)', 'Down (x^2 = -4ay)'])
    a = st.number_input("Enter the value for 'a' in the parabola equation", min_value=0.0, value=1.0)
    if orientation == 'Right (y^2 = 4ax)':
        y_vals = np.linspace(-5, 5, 400)
        x_vals = a * y_vals**2 / 4
    elif orientation == 'Left (y^2 = -4ax)':
        y_vals = np.linspace(-5, 5, 400)
        x_vals = -a * y_vals**2 / 4
    elif orientation == 'Up (x^2 = 4ay)':
        x_vals = np.linspace(-5, 5, 400)
        y_vals = a * x_vals**2 / 4
    elif orientation == 'Down (x^2 = -4ay)':
        x_vals = np.linspace(-5, 5, 400)
        y_vals = -a * x_vals**2 / 4
    plt.plot(x_vals, y_vals, color='r')

# Show the plot
st.pyplot(plt.gcf())
