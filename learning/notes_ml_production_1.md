# Notes from ML in Production - 1
I'm currently working through the [Machine Learning Engineering for Production (MLOps) Specialization](https://www.coursera.org/specializations/machine-learning-engineering-for-production-mlops) by deeplearning.ai. While much of this content is already familiar to me, I enjoy working through these classes to find new or interesting nuggets that I might have missed in my self-learning journey. This story is a set of notes and musings that capture the parts I wouldn't have picked up otherwise. Since I'm a threat intelligence nerd by day, I try to capture those parts particularly relevant to hunting bad actors.

## Class 1 - Intro to Machine Learning in Production
### Key takeaways:
- in adversarial environments data and concept drift are constant and fast, this applies to virtually all ML in the cyber security/intel space
- parts of the MLOPs toolchain such as data augmentation, can and will be used by bad actors for evasion, augmentation and evasion are related
- the purpose of many ML models is to match human level performance (HLP) rather than surpass it, what danger lurks in trying to do better?

### Course Overview
This class covers high level details around data and concept drift in building models. This intro course prompts you to ask if you have the right problems, the right data and make sure your approach is solid. This course brings perspective to people who have successfully trained an ML model in a Jupyter notebook and want to take those models forward into production. An optional part of the course goes deeper into the idea that just because you *can* train a model doesn't mean you *should*, i.e. does  it make sense in the real world.

### Adversarial Environments and Data/Concept drift
One takeaway from this course was how data and concept drift often lead models to perform poorly in the real world. This is presented as normal in building models, the world changes resulting in data and outcomes that change over time. In the context of adversarial environments, which is almost all of the security and threat intelligence domain, this process is accelerated. An adversarial environment in which a human attempts to bypass defenses will produce a constantly changing set of features that map to consistent labels. This leads to data drift and in many cases concept drift.

For example, imagine creating a model that can predict if...<tbc> 

### Data Augmentation and Evasion

### Beating Human Level Performance (HLP)
Keras generator can apply rotate, crop, etc automatically to augment data

Seems to be what is seen in the wild to evade naive models

Keras datasets can use directory structures to infer classes and build the datasets
sample_gen = ImageDataGenerator(

rescale=1./255,

rotation_range=50,

width_shift_range=0.25,

height_shift_range=0.25,

shear_range=0.2,

zoom_range=0.25,

horizontal_flip=True)