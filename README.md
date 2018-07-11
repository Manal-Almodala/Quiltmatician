# Quiltmatician

<p align="center">
  <img width="500" src="https://github.com/bbadh001/Quiltmatician/blob/master/assets/screenshot.png">
</p>

Quiltmatician is a fabric-cutting utility designed for quilters to minimize fabric used for cutting primitive shapes. 

When a quilter begins a new project, they first start by planning how many "primitives" (commonly squares) they will need. It is from these primitives other shapes and designs can be cut. When the number of primitives is very small, one can calculate (with little trouble) a cutting pattern and how much fabric they will need. However, when the number of primtives becomes non-trivial and varying their sizes vary, determining an optimal cutting pattern becomes _exponentially_ harder.

## How to run

Open terminal and run the following commands:

```
git clone https://github.com/bbadh001/Quiltmatician.git
cd Quiltmatician
python Quilt-matician.py
```

## Background

The problem is essentially a slightly modified (more on this later) version of the 2D cutting stock problem, which belongs to a greater class called Combinairoial Optimization problems. The basic idea is that you have some set of items you would like arrange on a rectangle of material such that the material wasted is minimized. 

It should be quite clear why this problem is so difficult. The number of possible packings on a 2D grid is typically too large, even for a relatively small number of items. Hence, we can't simply brute force search our way through the solution space to look for the optimal packing.  

Now is probbaly a good time to note that packing and cutting stock problems are in fact NP-hard problems. With this in mind, we shouldn't hold our breath trying to find efficient exact solution. One way around this is to devise a polynomial approximation algorithm. Like the name suggests, we can almost guarantee it will not arrive at the optimal solution, but we can hopefully arrive at a solution that is "good enough".

## A simple approach (to a hard problem)

A concept that comes up frequently when talking about approximation algorithms is this idea of a heuristic. A heuristic can be thought of as "rule of thumb" reasoning that helps arrive at an approximate solution efficiently without the guarantee of achieving the optimal solution. 

The algorithm I implemeneted involves the use of an incredibly simple, well-known heuristic called the first-fit decreasing (FFD) hurestic. FFD consists of sorting the shapes by their size in decreasing order and inserting them into the bin's next enpty location until no shapes are left. Superizngly, this heuristic works quite well and generates patterns that are in fact very tightly packed, hence use less material. 

## Pitfalls (and some thoughts on how to fix them)

There is one major caveat that I found unique to this problem. While this simple algorithm does genernate patterns
