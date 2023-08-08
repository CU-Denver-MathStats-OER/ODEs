# Preface
---

This collection of interactive Jupyter notebooks are intended as a set of activities for exploring models of differential equations and understanding their solutions (numerical, graphical, and analytical). Topics covered by these materials include first and second order differential equations, Laplace transforms, and systems of equations (linear and nonlinear). These materials serves as the textbook for the "MATH 3200: Elementary Differential Equations" course at University of Colorado Denver.


## A Virtual Lab for Experimenting with Differential Equations
---

These materials are intended as set of activities to experiment and explore differential equations. Each interactive Jupyter notebooks is a "virtual laboratory" where we perform our experiments and summarize the results. The objectives of experimental mathematics are generally to make mathematics **more tangible, lively and fun.**

The intent of introducing Python is not to avoid a deep and rigorous understanding of differential equations and simply use Python to solve differential equations. There are other sources that skim the concepts on the surface and focus on the coding side of things. These materials use Python as an additional tool for further exploring differential equations to gain a deeper insight into modeling with differential equations. Some of the objectives of implementing Python code cells into the materials are to:

- Discover patterns and relationships.
- Use graphical displays to investigate mathematical concepts.
- Develop and test conjectures.
- Explore results to help construct proofs.
- Confirm analytically derived results.
- Gain further insight and intuition.
- **Bridge the divide between theory and practice.**<


## How to Access, Edit and Save Notebooks
---

In addition to the each individual Jupyter notebook in this repo, there is a html version of the materials available at , <https://aspiegler.github.io/Exploring-Differential-Equations/>. You cannot edit the text or run code in the html version, but there is a link to each Jupyter notebook at the start of each section.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/CU-Denver-MathStats-OER/ODEs/blob/main/Chp1/01-What-is-a-Differential-Equation.ipynb)<nbsp>

- At the top of each notebook is a "button" such as the one above.
- Click the button to open an interactive Jupyter notebook version in [Google Colaboratory](https://colab.research.google.com/) (or Colab).
- You can begin working with the notebook right away in Colab! There is no software to install (or purchase!).
- You can also access the materials directly on GitHub at <https://github.com/CU-Denver-MathStats-OER/ODEs.git>.


Each Jupyter notebook contains both narrative text (in Markdown cells) and Python code cells that you can create, modify, and run. Although you do not need a Google account to interact with the notebooks, the Colab notebooks are "shared", meaning you cannot save any changes to the initial shared document that opens. **If you would like to save your changes, you first need to save a copy to your Google Drive.** Then you can edit and save changes to your own version.


## What Programming Background is Required?

---


No prior experience or knowledge of Python, Markdown, LaTeX, or Colaboratory is assumed or required to begin working with these materials. After working with these materials, you will have some knowledge and experience with Python, Markdown, LaTeX, and Colaboratory!

- [Welcome to Colaboratory](https://colab.research.google.com/notebooks/intro.ipynb) is a helpful notebook (with videos) to help introduce you to Colab.
- Here's a helpful [Markdown guide](https://colab.research.google.com/notebooks/markdown_guide.ipynb)


### What is Python?

---

We will be using [Python](https://www.python.org/) as a tool for experimenting with differential equations. Python is a widely used programming language suited for many purposes and applications such as computational mathematics, data science, and app development. We will create, modify, and run Python code in Jupyter notebooks. **No prior programming experience is required to begin working in Python in these materials.**

The goal of these materials are to investigate differential equations, not learn how to be an expert Python coder. The hope is that we can use Python as a tool for experimenting and gaining insight into  differential equations, and in the process, gain a familiarity with Python and coding so it is no longer a barrier. Have I mentioned **no prior programming experience is required to begin working in Python in these materials**?

There are two Python modules (`ode_tools.py` and `mass_spring.py`) that accompany these materials with scripts to perform certain tasks such as plotting slope fields, Euler's method, plotting phase planes, and widgets for experimenting with mass-spring systems. Whenever these modules are used, instructions are provided. There are more detailed instructions found:

- [Quick Reference for Python Functions: Chapter 1](https://githubtocolab.com/CU-Denver-MathStats-OER/ODEs/blob/main/Chp1/ODE-Tools-Tutorial.ipynb)
- [Quick Reference for Python Functions: Chapter 2](https://githubtocolab.com/CU-Denver-MathStats-OER/ODEs/blob/main/Chp2/Mass-Spring-Tutorial.ipynb)
- [Quick Reference for Python Functions: Chapter 3](https://githubtocolab.com/CU-Denver-MathStats-OER/ODEs/blob/main/Chp3/Phase-Portraits-Tutorial.ipynb)




### What is LaTex?

---

[LaTeX](https://www.cmor-faculty.rice.edu/~heinken/latex/symbols.pdf) is a system for rendering nice looking mathematical symbols, expressions, and equations. All of the mathematical notation in these materials are created using LaTeX. You can view and edit all of the LaTeX code in the Markdown cells. You do not need to become an expert in LaTeX, but having a familiarity with LaTeX is quite helpful and LaTeX can be used to typeset math in a number of different applications.

- Here is a useful [dictionary of LaTeX math symbols](https://www.cmor-faculty.rice.edu/~heinken/latex/symbols.pdf) to get a glimpse of LaTeX.


## A Remix of Inquiry-Oriented Differential Equations

---

Prior to creating these notebooks, I was teaching differential equation using Inquiry-Oriented Differential Equations (IODE) by Rasmussen, C., Keene, K. A., Dunmyre, J., & Fortune, N. IODE course materials are available at <https://iode.sdsu.edu>. The IODE content has been kindly shared by the authors for revising, remixing and redistributing.

- Some notebooks in these collection are not based on IODE content.
- Some notebooks are almost identical with IODE content. 
- Some sections are modifications of IODE materials.


**Much gratitude and thanks to the IODE team for creating and sharing amazing content with instructors and students of differential equations!** 

## Supplemental OER Texts

--- 

Below are two suggested Open Education Resources (OER) texts for a first course in differential equations for further reading.

- [Notes on Diffy Qs: Differential Equations for Engineers](https://www.jirka.org/diffyqs/) by Jiri Lebl.
- [Elementary Differential Equations](https://digitalcommons.trinity.edu/mono/8/) by William F. Trench


## How to Contact Me

---

If you have any questions, comments, or suggestions about these materials, please feel free to reach out to me (Adam) at [adam.spiegler@ucdenver.edu](mailto:adam.spiegler@ucdenver.edu).

- Considering using these materials in your course? Please let me know if I can help.
- If you do use some of these materials in your course, your feedback is welcome and appreciated.
- If you materials that you would like to share or contribute to this project, great!


# Table of Contents

---

## Chapter 1: First Order Differential Equations

---

- [01: What Is a Differential Equation?](https://githubtocolab.com/CU-Denver-MathStats-OER/ODEs/blob/main/Chp1/01-What-is-a-Differential-Equation.ipynb)

- [02: Slope Fields](https://githubtocolab.com/CU-Denver-MathStats-OER/ODEs/blob/main/Chp1/02-Slope-Fields.ipynb)

- [03: Phase Line](https://githubtocolab.com/CU-Denver-MathStats-OER/ODEs/blob/main/Chp1/03-Phase-Line.ipynb)

- [04: Euler's Method](https://githubtocolab.com/CU-Denver-MathStats-OER/ODEs/blob/main/Chp1/04-Eulers-Method.ipynb)

- [05: Separable Differential Equations](https://githubtocolab.com/CU-Denver-MathStats-OER/ODEs/blob/main/Chp1/05-Separable-Diff-Eqs.ipynb)

- [06: Integrating Factors](https://githubtocolab.com/CU-Denver-MathStats-OER/ODEs/blob/main/Chp1/06-Integrating-Factors.ipynb)

- [07: Application: Population and Compartmental Analysis](https://githubtocolab.com/CU-Denver-MathStats-OER/ODEs/blob/main/Chp1/07-Mixture-Applications.ipynb)

- [08: Application: Heating and Cooling Models](https://githubtocolab.com/CU-Denver-MathStats-OER/ODEs/blob/main/Chp1/08-Application-Heating-and-Cooling.ipynb)

- [Quick Reference Guide on How to Use Python Functions for Chapter 1](https://githubtocolab.com/CU-Denver-MathStats-OER/ODEs/blob/main/Chp1/ODE-Tools-Tutorial.ipynb)


## Chapter 2: Second Order Differential Equations

---

- [09: Introduction to Second Order Linear Differential Equations](https://githubtocolab.com/CU-Denver-MathStats-OER/ODEs/blob/main/Chp2/09-Intro-to-Second-Order.ipynb)

- [10: Homogeneous Second Order Differential Equations](https://githubtocolab.com/CU-Denver-MathStats-OER/ODEs/blob/main/Chp2/10-Homogeneous-2nd-Order.ipynb)

- [11: Nonhomogeneous Second Order Differential Equations](https://githubtocolab.com/CU-Denver-MathStats-OER/ODEs/blob/main/Chp2/11-Nonhomogeneous-2nd-Order.ipynb)

- [12: General Solutions to Nonhomogeneous Second Order Differential Equations](https://githubtocolab.com/CU-Denver-MathStats-OER/ODEs/blob/main/Chp2/12-Superposition-2nd-Order.ipynb)

- [13: Applications to Mass-Spring Systems](https://githubtocolab.com/CU-Denver-MathStats-OER/ODEs/blob/main/Chp2/13-Mass-Spring.ipynb)

- [Quick Reference for Mass Spring Animations in Chapter 2](https://githubtocolab.com/CU-Denver-MathStats-OER/ODEs/blob/main/Chp2/Mass-Spring-Tutorial.ipynb)


## Chapter 3: Systems of Differential Equations

---

- [14: Introduction to Systems of Differential Equations](https://githubtocolab.com/CU-Denver-MathStats-OER/ODEs/blob/main/Chp3/14-Introduction-to-Systems.ipynb)

- [15: Phase Plane Portrait](https://githubtocolab.com/CU-Denver-MathStats-OER/ODEs/blob/main/Chp3/15-Phase-Plane-Portrait.ipynb)

- [16: Phase Plane Equation](https://githubtocolab.com/CU-Denver-MathStats-OER/ODEs/blob/main/Chp3/16-Phase-Plane-Equation.ipynb)

- [17: Linear Systems of Differential Equations](https://githubtocolab.com/CU-Denver-MathStats-OER/ODEs/blob/main/Chp3/17-Linear-Systems.ipynb)

- [18: Stability of Equilibrium](https://githubtocolab.com/CU-Denver-MathStats-OER/ODEs/blob/main/Chp3/18-Stability-of-Equilibrium.ipynb)

- [19: Nonlinear Systems of Differential Euqations](https://githubtocolab.com/CU-Denver-MathStats-OER/ODEs/blob/main/Chp3/19-Nonlinear-Systems.ipynb)

- [Quick Reference hase Plane Portraits in Chapter3](https://githubtocolab.com/CU-Denver-MathStats-OER/ODEs/blob/main/Chp3/Phase-Portraits-Tutorial.ipynb)



## Chapter 4: Laplace Transforms

---

- [20: Introduction to Laplace Transforms](https://githubtocolab.com/CU-Denver-MathStats-OER/ODEs/blob/main/Chp4/20-Introduction-to-Laplace-Transforms.ipynb)

- [21: Properties of Laplace Transforms](https://githubtocolab.com/CU-Denver-MathStats-OER/ODEs/blob/main/Chp4/21-Properties-of-Laplace-Transforms.ipynb)

- [22: Inverse Laplace Transforms](https://githubtocolab.com/CU-Denver-MathStats-OER/ODEs/blob/main/Chp4/22-Inverse-Laplace-Transforms.ipynb)

- [23: Solving Differential Equations with Laplace Transforms](https://githubtocolab.com/CU-Denver-MathStats-OER/ODEs/blob/main/Chp4/23-Solving-IVP-with-Laplace-Transforms.ipynb)


## Acknowledgements

--- 

<img src="https://cdhe.colorado.gov/sites/highered/files/logo.svg" alt="Colorado Department of Higher Education"  width="30%">

This project was supported by the [Colorado Department of Higher Education (CDHE)](https://cdhe.colorado.gov/) OER Grant Program. A big thank you to Troy Butler, Jonathon Hirschi, and Dmitry Ostrovskiy for their feedback various contributions to these materials. Lastly, thanks to my students at CU Denver for all the feedback and encouragement in developing these materials!


## Creative Commons License Information

---

![Creative Commons License](https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png) <nbsp>

*Exploring Differential Equations* by [Adam Spiegler (University of Colorado Denver)](https://github.com/CU-Denver-MathStats-OER/Statistical-Theory) is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/). This work is funded by an [Institutional OER Grant from the Colorado Department of Higher Education (CDHE)](https://cdhe.colorado.gov/educators/administration/institutional-groups/open-educational-resources-in-colorado). Based on a work at <https://github.com/CU-Denver-MathStats-OER/ODEs> and original content created by Rasmussen, C., Keene, K. A., Dunmyre, J., & Fortune, N. (2018). *Inquiry oriented differential equations: Course materials*. Available at <a href="https://iode.sdsu.edu">https://iode.sdsu.edu</a>.


For similar interactive OER materials in other courses funded by this project in the Department of Mathematical and Statistical Sciences at the University of Colorado Denver, visit <https://github.com/CU-Denver-MathStats-OER>.



