# CPU vs GPU vs TPU

```{admonition} Additional Reads:
:class: tip
- [TPU presentation from Google](https://storage.googleapis.com/nexttpu/index.html)
- [TPU architecture in details](https://cloud.google.com/tpu/docs/system-architecture)
```

According to [John Henssey](https://en.wikipedia.org/wiki/John_L._Hennessy), father of modern computer, we are almost at an end of Moores's law. End of exponential growth in CPU and he suggested domain specific software as the solution.

```{figure} ./image2.PNG
---
height: 250px
name: image1
---
```

## How does a CPU work?

The CPU is a general purpose processor based on the von Neumann architecture. The greatest benefit of CPU is its flexibility. With its Von Neumann architecture, you can load any kind of software for millions of different applications. You could use a CPU for word processing in a PC, controlling rocket engines, executing bank transactions, or classifying images with a neural network.

But, because the CPU is so flexible, the hardware doesn't always know what would be next calculation until it reads the next instruction from the software. A CPU has to store the calculation results on memory inside CPU (so called registers or L1 cache) for every single calculation. This memory access becomes the downside of CPU architecture called the von Neumann bottleneck. Even though the huge scale of neural network calculations means that these future steps are entirely predictable, each CPU's Arithmetic Logic Units (ALU, the component that holds and controls multipliers and adders) executes them one by one, accessing the memory every time, limiting the total throughput and consuming significant energy.

```{figure} ./image1.PNG
---
height: 250px
name: image2
---
von Neumann Architecture
```

Since memory and the CPU are separated in this architecture, the performance of the system is often limited by the speed of accessing memory. Historically, the memory access speed is orders of magnitude slower than the actual processing speed, creating a bottleneck in the system performance.

Furthermore, the physical movement of data consumes a significant amount of energy due to interconnect parasitics. In given situations, it has been observed that the physical movement of data from memory can consume up to 500 times more energy than the actual processing of that data. This trend is only expected to worsen as chips scale.

## How does a GPU work?

To gain higher throughput than a CPU, a GPU uses a simple strategy: why not have thousands of ALUs in a processor? The modern GPU usually has 2,500–5,000 ALUs  in a single processor that means you could execute thousands of multiplications and additions simultaneously.

This GPU architecture works well on applications with massive parallelism, such as matrix multiplication in a neural network. Actually, you would see order of magnitude higher throughput than CPU on typical training workload for deep learning. This is why the GPU is the most popular processor architecture used in deep learning at time of writing.

But, the GPU is still a general purpose processor that has to support millions of different applications and software. This leads back to our fundamental problem, the von Neumann bottleneck. For every single calculation in the thousands of ALUs, GPU need to access registers or shared memory to read and store the intermediate calculation results. Because the GPU performs more parallel calculations on its thousands of ALUs, it also spends proportionally more energy accessing memory and also increases footprint of GPU for complex wiring.
     

## How does a TPU work?

When Google designed the TPU, we built a domain-specific architecture. That means, instead of designing a general purpose processor, we designed it as a matrix processor specialized for neural network work loads. TPUs can't run word processors, control rocket engines, or execute bank transactions, but they can handle the massive multiplications and additions for neural networks, at blazingly fast speeds while consuming much less power and inside a smaller physical footprint.

The key enabler is a major reduction of the von Neumann bottleneck. Because the primary task for this processor is matrix processing, hardware designer of the TPU knew every calculation step to perform that operation. So they were able to place thousands of multipliers and adders and connect them to each other directly to form a large physical matrix of those operators. This is called systolic array architecture. In case of Cloud TPU v2, there are two systolic arrays of 128 x 128, aggregating 32,768 ALUs for 16 bit floating point values in a single processor.

Let's see how a systolic array executes the neural network calculations. At first, TPU loads the parameters from memory into the matrix of multipliers and adders.

Then, the TPU loads data from memory. As each multiplication is executed, the result will be passed to next multipliers while taking summation at the same time. So the output will be the summation of all multiplication result between data and parameters. During the whole process of massive calculations and data passing, no memory access is required at all.

This is why the TPU can achieve a high computational throughput on neural network calculations with much less power consumption and smaller footprint.

```{figure} ./image3.PNG
---
height: 300px
name: image3
---
CPU vs GPU vs TPU
```
