# Neural Network

{% hint style="success" %}
[This is an excellent resource available for free on Neural Networks](http://neuralnetworksanddeeplearning.com/chap1.html)
{% endhint %}

Perceptrons were one of the earliest proposed models for learning simple classification tasks, which later became the fundamental building block of artificial neural networks.

## Artificial Neuron

An artificial neuron is very similar to a perceptron, except that the activation function is not a step function.

Like a perceptron, the input is the weighted sum of inputs. The output is the activation function applied on the input. The activation function could be any function, though it should have some important properties such as:

* Activation functions should be smooth i.e. they should have no abrupt changes when plotted
* They should also make the inputs and outputs non-linear with respect to each other to some extent. This is because non-linearity helps in making neural networks more compact

Some of the common activation functions are as follows:

<figure><img src="../_build/html/_images/image110.PNG" alt=""><figcaption><p><a href="https://www.v7labs.com/blog/neural-networks-activation-functions">Source</a></p></figcaption></figure>

**An artificial neural network is a network of such neurons.** Neurons in a neural network are arranged in layers. The _first_ and the _last_ layer are called the _input_ and _output_ layers. Input layers have as many neurons as the number of attributes in the data set and the output layer has as many neurons as the number of classes of the target variable (for a classification problem). For a regression problem, the number of neurons in the output layer would be 1 (a numeric variable). There are six main things that need to be specified for specifying a neural network completely:

* Network Topology
* Input Layer
* Output Layer
* Weights
* Activation functions
* Biases

An important thing to note is that the inputs can only be numeric. For different types of input data, we use different ways to convert the inputs to a numeric form. In case of text data, we either use a one-hot vector or word embeddings corresponding to a certain word. Feeding images (or videos) is straightforward since images are naturally represented as arrays of numbers.

**The output layer used in case of multiclass classification problem is the softmax layer.** A softmax output is a multiclass logistic function commonly used to compute the 'probability' of an input belonging to one of the multiple classes.

Since large neural networks can potentially have extremely complex structures, certain assumptions are made to simplify the way information flows in them:

* Neurons are arranged in layers and the layers are arranged sequentially
* Neurons within the same layer do not interact with each other
* All the inputs enter the network through the input layer and all the outputs go out of the network through the output layer
* Neurons in consecutive layers are densely connected, i.e. all neurons in layer $$l$$ are connected to all neurons in layer $$l+1$$
* Every interconnection in the neural network has a weight associated with it, and every neuron has a bias associated with it
* All neurons in a particular layer use the same activation function

Neural networks require rigorous training. Recall that models such as linear regression, logistic regression, SVMs etc. are trained on their coefficients, i.e. the training task is to find the optimal values of the coefficients to minimize some cost function. Neural networks are no different - they are trained on weights and biases.

During training, the neural network learning algorithm fits various models to the training data and selects the best model for prediction. The learning algorithm is trained with a fixed set of hyperparameters - the network structure (number of layers, number of neurons in the input, hidden and output layers etc.). It is trained on the weights and the biases, which are the parameters of the network.

<figure><img src="../_build/html/_images/image2.gif" alt=""><figcaption><p>Neural Networks can be used to <em>reasonably</em> approximate <em>most</em> functions</p></figcaption></figure>

## Feed forward

In artificial neural networks, the output from one layer is used as input to the next layer. Such networks are called feedforward neural networks. Feed forward neural network architecture consists of following main parts – Input Layer, Hidden Layer - If the number of hidden layers is one then it is known as a shallow neural network, else it is known as a deep neural network, Output Layer

<figure><img src="../_build/html/_images/image3.gif" alt=""><figcaption><p><a href="https://machinelearningknowledge.ai/animated-explanation-of-feed-forward-neural-network-architecture/">Source</a></p></figcaption></figure>

## Backpropagation

In the neural network training task, the goal is to compute the optimal weights and biases by minimizing some cost function. The task of training neural networks is exactly the same as that of other ML models such as linear regression, SVMs etc. The desired output (output from the last layer) minus the actual output is the cost (or the loss), and we to tune the parameters $$w$$ and $$b$$ such that the total cost is minimized.

An important point to note is that if the data is large (which is often the case), loss calculation itself can get pretty messy. For example, if you have a million data points, they will be fed into the network (in batches), the output will be calculated using feedforward and the loss/cost $$L_i$$ (for $$i^{th}$$ data point) will be calculated. The total loss is the sum of losses of all the individual data points. We minimize the average of the total loss and the not the total loss. Minimizing the average loss implies that the total loss is getting minimized.

For a large neural network, the number of weight elements and biases becomes so large and minimizing the loss with so many parameters is a difficult task. This complex task is achieved using gradient descent.

<figure><img src="../_build/html/_images/image4.gif" alt=""><figcaption><p><a href="https://machinelearningknowledge.ai/animated-explanation-of-feed-forward-neural-network-architecture/">Source</a></p></figcaption></figure>

For updating weights and biases using plain backpropagation, you have to scan through the entire data set to make a single update to the weights. This is computationally very expensive for large datasets. Thus, you use multiple batches (or **mini-batches**) of data points, compute the average gradient for a batch, and update the weights based on that gradient.

But there is a danger in doing this - you are making weight updates based only on gradients computed for small batches, not the entire training set. Thus, you make multiple passes through the entire training set using epochs. An epoch is one pass through the entire training set, and you use multiple epochs (typically 10, 20, 50, 100 etc.) while training. In each epoch, you reshuffle all the data points, divide the reshuffled set into m batches, and update weights based on gradient of each batch.

### Stochastic Gradient Descent (SGD)

In most libraries such as TensorFlow, the SGD training procedure is as follows:

* You specify the number of epochs (typical values are 10, 20, 50, 100 etc.) - more epochs require more computational power
* You specify the number of batches $$m$$ (typical values are 32, 64, 128, etc.)
* At the start of each epoch, the data set is reshuffled and divided into $$m$$ batches
* The average gradient of each batch is then used to make a weight update
* The training is complete at the end of all the epochs

Apart from being computationally faster, the SGD training process has another big advantage - it actually helps you reach the global minima (instead of being stuck at a local minima). Also, to avoid the problem of getting stuck at a local optimum, you need to strike a balance between exploration and exploitation. Exploration means that you try to minimize the loss function with different starting points of $$W$$ and $$b$$, i.e., you initialize $$W$$ and $$b$$ with different values. On the other hand, exploitation means that you try to reach the global minima starting from a particular  $$W$$ and $$b$$ and do not explore the terrain at all. That might lead you to the lowest point locally, but not the necessarily the global minimum.

## Modifications in Neural Networks

Neural networks are usually large, complex models with tens of thousands of parameters, and thus tend to overfit the training data. As with many other ML models, regularization is a common technique used in neural networks to address this problem.

The _parameter norm_ regularization is similar to that in linear regression in almost every aspect. As in lasso regression (L1 norm), we get a sparse weight matrix, which is not the case with the L2 norm. Despite this fact, the L2 norm is more common because the sum of the squares term is easily differentiable which comes in handy during backpropagation. Apart from using the parameter norm, there is another popular neural network regularization technique called **dropouts**.

### Dropouts

Some important points to note regarding dropouts are:

* Dropouts can be applied only to some layers of the network (in fact, that is a common practice - you choose some layer arbitrarily to apply dropouts to)
* The mask $$\alpha$$ is generated independently for each layer during feedforward, and the same mask is used in backpropagation.
* The mask changes with each minibatch/iteration, are randomly generated in each iteration (sampled from a Bernoulli with some $$p(1)=q$$)

Why the dropout strategy works well is explained through the notion of a manifold. Manifold captures the observation that in high dimensional spaces, the data points often actually lie in a lower-dimensional manifold. The dropout strategy uses this fact to find a lower-dimensional solution to the problem.

Dropouts help in symmetry breaking as well. There is every possibility of the creation of communities within neurons which restricts them from learning independently. Hence, by setting some random set of the weights to zero in every iteration, this community/symmetry is broken. Note that there, a different mini batch is processed in every iteration in an epoch, and dropouts are applied to each mini batch.

### Problems

<details>

<summary>Vanishing and Exploding Gradient</summary>

Explain the vanishing and exploding gradient problem in neural networks.

**Answer**

The vanishing and exploding gradient problems are issues that can occur during the training of deep neural networks, particularly in deep feedforward neural networks and recurrent neural networks (RNNs). These problems are related to the way gradients (derivatives of the loss function with respect to the model parameters) are propagated backward through the layers of a network during the training process using gradient descent or its variants.

1. **Vanishing Gradient Problem:**
   * The vanishing gradient problem occurs when the gradients of the loss function with respect to the model parameters become very small as they are propagated backward through the layers of a deep network.
   * This is problematic because small gradients lead to very slow weight updates during training, which can result in the network learning very slowly or not learning at all.
   * It typically occurs in networks with many layers, especially when activation functions like sigmoid or hyperbolic tangent (tanh) are used.
   * These activation functions squash their inputs into a small range, and the derivatives of these functions become very small for large or very small inputs. As gradients are backpropagated, these small gradients can compound, making earlier layers learn very slowly.
2. **Exploding Gradient Problem:**
   * The exploding gradient problem is the opposite of the vanishing gradient problem. It occurs when gradients become extremely large as they are propagated backward through the layers of a deep network.
   * When gradients are too large, they can lead to numerical instability during training, causing the model's weights to become NaN (Not-a-Number) or saturate, which can hinder convergence.
   * The exploding gradient problem can happen in networks with certain types of architectures, large learning rates, or poorly conditioned loss functions.

Solutions to these problems include:

**1. Weight Initialization:** Properly initializing the weights of neural networks can help alleviate the vanishing and exploding gradient problems. Techniques like He initialization or Xavier initialization set initial weights to values that help maintain gradient magnitudes.

**2. Activation Functions:** Using activation functions that have gradients that neither vanish nor explode across a wide range of inputs can help. Rectified Linear Units (ReLUs) are popular because they don't saturate for positive inputs.

**3. Batch Normalization:** Batch normalization normalizes the inputs to each layer, reducing internal covariate shift and helping gradients flow more consistently during training.

**4. Gradient Clipping:** This technique limits the magnitude of gradients during training to prevent them from becoming too large and causing the exploding gradient problem.

**5. Architecture Design:** Using skip connections or residual connections in deep networks can help gradients flow more easily through the network.

**6. Learning Rate Scheduling:** Adjusting the learning rate during training, such as using learning rate annealing or adaptive learning rate methods like Adam, can mitigate both problems.

These techniques collectively help mitigate the vanishing and exploding gradient problems and allow for the successful training of deep neural networks. The choice of which technique to use often depends on the specific network architecture and problem domain.

</details>

<details>

<summary>Perceptron</summary>

What is a perceptron?

**Answer**

* A **Perceptron** is a fundamental unit of a Neural Network that is also a single-layer Neural Network.
* Perceptron is a linear _classifier_. Since it uses already labeled data points, it is a _supervised learning algorithm_.
* The _activation function_ applies a step rule (convert the numerical output into +1 or -1) to check if the output of the weighting function is greater than zero or not.

A **Perceptron** is shown in the figure below:

<img src="../.gitbook/assets/image (1) (1).png" alt="" data-size="original">

</details>

<details>

<summary>Classify email into spam or ham</summary>

How many neurons needed to classify and email spam vs ham?

**Answer**

To classify email into spam or ham, you just need one neuron in the output layer of a neural network. For example, to indicate the probability that the email is spam, you would typically use the **logistic activation** function in the output layer when estimating a probability.

</details>

<details>

<summary>Role of Activation function</summary>

Can you explain the role of Activation function in NN?

**Answer**

* **Activation Functions** help in keeping the value of the output from the neuron restricted to a certain limit as per the requirement. If the limit is not set then the output will reach very high magnitudes. Most activation functions convert the output to `-1` to `1` or to `0` to `1`.
* The most _important_ role of the activation function is the ability to add **non-linearity** to the neural network. Most of the models in real-life is non-linear so the activation functions help to create a non-linear model.
* The _activation function_ is responsible for deciding whether a neuron should be activated or not.

</details>

<details>

<summary>Detect if a model has Vanishing Gradient Problem</summary>

How do you tell if your model has a Vanishing Gradient Problem?

**Answer**

* The model will improve _very slowly_ during the training phase and it is also possible that training stops _very early_, meaning that any further training does not improve the model.
* The weights closer to the output layer of the model would witness more of a change whereas the layers that occur closer to the input layer would not change much (if at all).
* Model weights _shrink exponentially_ and become _very small_ when training the model.
* The model weights become `0` in the training phase.

</details>

<details>

<summary>Detect if model has an Exploding Gradient Problem?</summary>

How do you tell if your model has an Exploding Gradient Problem?

**Answer**

There are some subtle signs that you may be _suffering from exploding gradients_ during the training of your network, such as:

* The model is unable to get traction on your training data (e g. _poor loss_).
* The model is _unstable_, resulting in large changes in loss from update to update.
* The model loss goes to `NaN` during training.

If you have these types of problems, you can dig deeper to see if you have a problem with exploding gradients. There are some less subtle signs that you can use to confirm that you have exploding gradients:

* The model weights quickly become very large during training.
* The model weights go to `NaN` values during training.
* The error gradient values are consistently above `1.0` for each node and layer during training.

</details>

<details>

<summary>Importance of initialization</summary>

Why is the initialization process important in neural network and explain some common initialization techniques?

**Answer**

The initialization process in neural networks is crucial because it sets the initial values for the model's parameters (weights and biases). Proper initialization can significantly impact the training process and the performance of the neural network. Here's why initialization is important:

1. **Avoiding Symmetry**: In neural networks, each neuron's parameters should have different initial values to break symmetry. If all neurons start with the same weights, they will all learn the same features, making the network no better than a single neuron. Proper initialization helps break this symmetry, allowing neurons to specialize in different features.
2. **Preventing Vanishing and Exploding Gradients**: Initializing weights properly can help mitigate the vanishing and exploding gradient problems, which can affect the stability and convergence of training.
3. **Faster Convergence**: Proper initialization can lead to faster convergence during training. A well-initialized network often requires fewer epochs to achieve good performance.

Here are some common weight initialization techniques used in neural networks:

1. **Zero Initialization**: Initializing all weights to zero is generally not recommended because it results in symmetric weights, causing all neurons to compute the same output. However, biases can be initialized to zero without much concern.
2. **Random Initialization**: This is the most common initialization technique. Weights are initialized with small random values. Some variations of random initialization include:
   * **Random Uniform Initialization**: Weights are sampled from a uniform distribution within a small range, such as \[-0.1, 0.1].
   * **Random Normal Initialization**: Weights are sampled from a normal distribution with a mean of 0 and a small standard deviation.
3. **Xavier/Glorot Initialization**: This initialization method is designed to work well with activation functions like the hyperbolic tangent (tanh) and the logistic sigmoid. It scales the initial weights based on the number of input and output units of a layer to maintain a consistent variance of activations throughout the network. The formula for Xavier initialization is:
   * For a layer with `n_in` input units and `n_out` output units:
     * Initialize weights from a random distribution with mean 0 and variance `2 / (n_in + n_out)`.
4. **He Initialization**: This initialization method is suitable for networks that use Rectified Linear Units (ReLUs) as activation functions. It scales the initial weights based on the number of input units to maintain a consistent variance of activations. The formula for He initialization is:
   * For a layer with `n_in` input units:
     * Initialize weights from a random distribution with mean 0 and variance `2 / n_in`.
5. **LeCun Initialization**: This initialization method is designed for networks using the Leaky ReLU activation function. It scales the initial weights based on the number of input units to maintain a consistent variance of activations. The formula for LeCun initialization is:
   * For a layer with `n_in` input units:
     * Initialize weights from a random distribution with mean 0 and variance `1 / n_in`.

Choosing the right initialization method depends on the specific neural network architecture, the choice of activation functions, and the problem at hand. Proper initialization can improve the network's training stability and convergence, making it an essential component of building effective neural networks.

</details>
