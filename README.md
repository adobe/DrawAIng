# DrawAIng

### Authors and Maitainers
Nandan Jha ( @jhanandan )
Sourabh Gupta ( @sourabhgupta01 )
Vikas Kumar ( @vikasmishra11 )
Piyush Singh ( @singpiyush )

## Introduction

DrawAIng is a ML based solution for autocompletion of sketches. It predicts finished sketches based on rough sketches drawn by user.

## Tech used 

* Model used : "AlexNet" https://github.com/val-iisc/sketch-object-recognition/tree/master/models/eitz/160/CNN/Alexnet

* Dataset used: http://cybertron.cg.tu-berlin.de/eitz/projects/classifysketch/
  The sketch dataset is licensed under a Creative Commons Attribution 4.0 International License.
  @article{
    eitz2012hdhso,
    author={Eitz, Mathias and Hays, James and Alexa, Marc},
    title={How Do Humans Sketch Objects?},
    journal={ACM Trans. Graph. (Proc. SIGGRAPH)},
    year={2012},
    volume={31},
    number={4},
    pages = {44:1--44:10}
  }

## Usage 

1. Clone the repository
2. Download Model from : 
   https://github.com/val-iisc/sketch-object-recognition/tree/master/models/eitz/160/CNN/Alexnet 
   and copy it to path app/model
3. Add your Result dataset in folder app/dataset
4. Run docker-compose up --build
5. To prepare and load  dataset run curl http://localhost:5000/createdataset
6. To make prediction run :  curl -F image=@"filepath"  http://localhost:5000/predict


### Contributing

Contributions are welcomed! Read the [Contributing Guide](./.github/CONTRIBUTING.md) for more information.

### Licensing

This project is licensed under the Apache V2 License. See [LICENSE](LICENSE) for more information.
