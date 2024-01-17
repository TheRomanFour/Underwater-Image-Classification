# Underwater-Image-Classification

 As part of the Realizor 2023 student case study competition for the company Vectrino, our project focuses on classifying images as good or bad (underwater/above water), with a specific emphasis on identifying undesirable photos containing ropes or similar objects underwater.



## Table of Contents

- [Idea](#idea)
- [How it Works](#how-it-works)
- [Development](#development)
- [Results](#results)
- [Conclusion](#conclusion)

## Idea

The goal of this project is to optimize the process of creating digital twins of underwater structures by efficiently filtering out unnecessary photos. Despite the success of capturing high-quality images, a significant percentage of them (8%) are unusable. The team proposes a solution that leverages artificial intelligence, specifically Convolutional Neural Networks (CNN), to automatically classify photos as good or bad.

## How it Works

### Convolutional Neural Network (CNN)

The solution is based on a deep learning approach using CNNs. These networks are trained to automatically recognize and classify visual characteristics of photos, enabling efficient sorting.

## Development

### Data Collection

Two comprehensive datasets, provided by Vectrino, were used for training and testing the model. The training set consisted of 3000 good and 3000 bad images, while the testing set was used to evaluate the model's reliability.

### Model Construction

The CNN model was built using Keras within the TensorFlow framework. Special techniques, such as dropout layers and early stopping, were employed to prevent overfitting during training.

### Training the Model

The model was trained using dynamic learning rate adjustment and early stopping techniques. The iterative training process aimed to adjust model weights to minimize the loss function on the training dataset while evaluating its generalization on the validation dataset.

## Results

The model was tested on a set of 6074 images, achieving impressive results. It classified 887 images, reducing the manual workload by 85%. The solution demonstrates significant time savings, especially when applied to larger datasets.

## Conclusion

While the CNN implementation showed success in classifying underwater photos, challenges such as misclassification of water surface patterns were identified. Further improvement can be achieved by enriching the dataset with diverse and challenging images. Future enhancements may focus on collecting more labeled data, utilizing better computing resources, and refining the model for superior performance in analyzing and classifying underwater photos.

