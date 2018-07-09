# Quiltmatician

<p align="center">
  <img width="500" src="https://github.com/bbadh001/Quiltmatician/blob/master/assets/screenshot.png">
</p>

Quiltmatician is a fabric-cutting utility designed for quilters to minimize fabric used for cutting primitive shapes. 

When a quilter begins a new project, they first start by planning how many "primitives" (commonly squares) they will need. It is from these primitives other shapes and designs can be cut. When the number of primitives is small, one can calculate (with little trouble) a cutting pattern and how much fabric they will need. However, when the number of primtives becomes non-trivial and varying their sizes vary, determining an optimal cutting pattern becomes _exponentially_ harder.

## How to run

Open terminal and run the following commands:

```
git clone https://github.com/bbadh001/Quiltmatician.git
cd Quiltmatician
python Quilt-matician.py
```

## Background

The problem is essentially a slightly modified (more on this later) version of the 2D cutting stock problem, which belongs to a greater class called Combinairoial Optimization problems. The basic idea is that you have some set of items you would like arrange on a material such that the material needed is to be minimized. 

It should be quite clear why this problem is so difficult. The number of possible packings a 2D grid is typically too large, even for relatively small number of items. Hence, 


