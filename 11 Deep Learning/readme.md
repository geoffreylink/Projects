## Reference

* [deepschool.io](https://github.com/RyanSydney/deepschool.io)
* [Easy Tensorflow](http://www.easy-tensorflow.com)
* [deeplearning.ai](https://www.deeplearning.ai)
* [Deep Dive into Math Behind Deep Networks](https://towardsdatascience.com/https-medium-com-piotr-skalski92-deep-dive-into-deep-networks-math-17660bc376ba)

## Entropy

![](https://github.com/geoffreylink/Projects/blob/master/11%20Deep%20Learning/images/Entropy.jpg)

## Batch Normalization

![](https://github.com/geoffreylink/Projects/blob/master/11%20Deep%20Learning/images/BatchNormalization.png)

## Activation Functions

Activation functions play a key role in every neural network. They decide which nodes to fire in a particular layer. These functions are applied to hidden as well as to the output layers of a neural network.

Activation functions take the weighted sum of inputs plus a bias as input to the function (w(i)*x(i)+b) and perform the necessary computation to decide which nodes to fire in a layer.

There are 5 popular activation functions that play a significant role in building a neural network. Choosing the right activation function depends on the kind of task you are performing.

* __Step function__ - also known as a Threshold function. Here we set a threshold value and if the Y value(output) is greater than the threshold value, the function is activated and fired, else it is not fired.

![](https://github.com/geoffreylink/Projects/blob/master/11%20Deep%20Learning/images/StepFunction.png)

* __ReLU function__ - one of the most widely used activation functions. It stands for Rectified Linear Unit. It gives an output of X, if X is positive and 0 otherwise. ReLU is often used in the hidden layers.

![](https://github.com/geoffreylink/Projects/blob/master/11%20Deep%20Learning/images/ReLUFunction.png)

* __Sigmoid function__ - very common and is used to predict the probability as an output. The output of this function always lies between 0 and 1. Sigmoid is used in hidden layers as well as in the output layers where the target is binary.

![](https://github.com/geoffreylink/Projects/blob/master/11%20Deep%20Learning/images/SigmoidFunction.png)

* __Tanh function__ - similar to a Sigmoid function but is bound between the range (-1, 1). It is also used in the hidden layers as well as in the output layer.

![](https://github.com/geoffreylink/Projects/blob/master/11%20Deep%20Learning/images/TanhFunction.png)

* __Softmax function__ - generally used in the output layer. It converts every output to been in the range of 0 and 1, just like the Sigmoid function. But it divides each output such that the total sum of the outputs is equal to 1.

![](https://github.com/geoffreylink/Projects/blob/master/11%20Deep%20Learning/images/SoftmaxFunction.png)

* __Artificial Neural Network__

![](https://github.com/geoffreylink/Projects/blob/master/11%20Deep%20Learning/images/ArtificialNeuralNetwork.png)

* __Human Neural Network__

![](https://github.com/geoffreylink/Projects/blob/master/11%20Deep%20Learning/images/HumanNeuralNetwork.png)
