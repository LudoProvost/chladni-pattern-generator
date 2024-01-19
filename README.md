# Chladni pattern generator
This is an algorithm that was done quickly and just for fun, the code is extremely messy. 
The goal was to generate Chladni pattern in 2 different ways: 
1. continuously on a PySimpleGUI window with as many FPS as possible.
2. a short high-quality GIF.

The overall goal was to produce visually appealing short animations and give myself an optimization challenge to see the maximum FPS I could reach.

## How it works
Chladni patterns are generated using a simple formula which takes for inputs an x and y coordinate and 4 variables (a,b,n,m). a,b,n, and m can take values between -10 and 10 (approximately).

## Results
### Continuous generation:
This was the hardest part as I wanted the continuous generation to evolve randomly over time. For this, i made certain constraints dictating how each of the 4 variables (a,b,n,m) can change over time. 
This lead to continuous and **random** generation of Chladni patterns, but it can sometimes be repetitive if only one of the variable decides to change back and forth for multiple seconds.

"@JIT" was used to optimize the repetitive calculations done on each pixel.

**The best quality achieved was ~20 FPS @ 1280x720p**, which was an improvement to the ~7 FPS i was getting at the same resolution *without* the use of JIT.

### High-quality GIF
This was exetremely easy to do with the help of the MoviePy library to create .gif files. The speed, resolution and quality can easily be changed to provide smoother GIFs than seen below.

## Generated Chladni patterns in GIF
![chladni](https://github.com/LudoProvost/chladni-pattern-generator/assets/70982826/b9f58c11-162d-4f78-8b54-c0231e6e3b0e)
![chladni_var_afrom-10to10](https://github.com/LudoProvost/chladni-pattern-generator/assets/70982826/c3805ea3-d011-41a4-b83c-f88c1cbb9757)
![chladni_var_bfrom-2to2](https://github.com/LudoProvost/chladni-pattern-generator/assets/70982826/d991f447-1c1a-4f88-9070-082b8081e50b)
![chladni_var_m](https://github.com/LudoProvost/chladni-pattern-generator/assets/70982826/546223bf-df5b-4f28-befe-35e4d0534d8b)
![chladni_var_n](https://github.com/LudoProvost/chladni-pattern-generator/assets/70982826/e2e61eaa-54d0-483b-9fcc-f27b0987bb24)

## Reference
[Creating digital Chladni patterns](https://thelig.ht/chladni/)
