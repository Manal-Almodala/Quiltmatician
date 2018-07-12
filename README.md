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

The problem is essentially a slightly modified (more on this later) version of the 2D cutting stock problem, which belongs to a greater class called Combinatorial Optimization problems. The basic idea is that you have some set of items you would like arrange on a rectangle of material such that the material wasted is minimized. 

It should be quite clear why this problem is so difficult. The number of possible packings on a 2D grid is typically too large, even for a relatively small number of items. Hence, we can't simply brute force search our way through the solution space to look for the optimal packing.  

Now is probbaly a good time to note that packing and cutting stock problems are in fact NP-hard problems. With this in mind, we shouldn't hold our breath trying to find efficient exact solution. One way around this is to devise a polynomial approximation algorithm. Like the name suggests, we can almost guarantee it will not arrive at the optimal solution, but we can hopefully arrive at a solution that is "good enough".

## A simple approach (to a hard problem)

A concept that comes up frequently when talking about approximation algorithms is this idea of a heuristic. A heuristic can be thought of as "rule of thumb" reasoning that helps arrive at an approximate solution efficiently without the guarantee of achieving the optimal solution. 

The algorithm I implemented involves the use of an incredibly simple, well-known heuristic called the first-fit decreasing (FFD) hurestic. FFD consists of sorting the shapes by their size in decreasing order and inserting them into the bin's next empty location until no shapes are left. Surprisingly, this heuristic works quite well and generates patterns that are in fact very tightly packed, hence use less material. 

## Pitfalls (and some thoughts on how to fix them)

There is one major caveat that I found unique to this problem. While the current algorithm does generate patterns that appear to minimize material length, it never considers the placement of cutting lines. If it were the case that we could give these cutting patterns to a machine to cut, then by not considering the cutting lines is something that does not pose a problem. However, if we expect a quilter to cut these patterns out by hand, they should at least be manageable to cut. Yet, because cutting lines are never factored into the algorithm, we could potentially generate patterns that are perfectly optimized with respect to length but have extremely convoluted cutting lines, making them virtually impossible for a human to cut by hand. 

I have considered a few possible solutions to this problem. The first would be to keep the current algorithm and add some additional logic for minimizing cutting length. One way I'd imagine this could be done is before placing a shape, you could check to see if an adjacent spot (N spaces away) would reduce the cutting line length and if it does, place it there. One problem with this is I could imagine there would have to be a trade-off between cutting line length and packing tightness, and determining this tradeoff apriori could be difficult. 

A second approach would be to scrap the current algorithm all together and opt for an algorithm that tends to produce straighter cutting lines naturally. An example of an algorithm that tends to do this naturally is level algorithms, which split the bin into horizontal levels and packs each level until they are filled. This looks hopeful as each horizontal level tends to maintain straighter cutting lines. The upside of this approach is that the algorithm tends to minimize cutting lines on its own and we wouldn't have to consider an explicit solution to this problem. However, it's upside is likely its downfall. Not expliciting considering the cutting lines is likely not going to produce going to produce the best solution. 

A third approach would be devising some sort of genetic algorithm. This approach would probably require the most research and implementation time but I would suspect this would produce a very good solution




