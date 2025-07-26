# Sundial Generator 🕰️

This project is a sundial drawing tool developed to explore the geometric and astronomical principles behind different types of sundials. It calculates hour lines for several sundial types based on user input, using spherical astronomy and projection geometry.

## 🌍 Overview

I have always been fascinated by sundials as a form of ancient knowledge and scientific craftsmanship. This tool allowed me to dive into their mathematical foundations and produce accurate graphical representations.

Currently, the program supports:

* **Horizontal sundials**
* **Equatorial sundials**
* **Vertical sundials (declining walls)**

The implementation is focused on **French hours**. Future versions may include **Italian hours** (sunset-based) and **Babylonian hours** (sunrise-based).

## 🧮 Features

* Calculates sundial based on:

  * Latitude
  * Wall declination
  * Solar geometry

* And in particular:

  * you can focus on a particular month
  * you can focus on a particular day of a month

* Supports arbitrary orientations of the wall
* Supports arbitrary orientations of the gnomon

And:

* Generates graphical output (e.g., plot or vector drawing)
* Generates numerical coordinates so that one can draw a real sundial!

## 💻 Libraries Used

The code is very simple because the most important part of the development was about the matemathical part. I only used:

* NumPy for trigonometric calculations
* Matplotlib (or similar) for visual output

## 🚀 Code

The current state of the code is not up-to-date. You can still run the code and have an horizontal sundial. If you want the full version you can contact me.

