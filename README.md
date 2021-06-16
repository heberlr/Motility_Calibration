# Motility_Calibration
This code makes the calibration of a PhysiCell model according to the displacement of tumor-derived cells. We use Bayesian inference to calibrate the speed and bias of cells, using the LF-MCMC method (Marjoram et al., 2003). Scripts to generate figures are available in this repository.

This model is part of a collaboration between Dr. Macklin's lab and Dr. Gilkes's lab, through of a project granted by Jayne Koskinas Ted Giovanis (JKTG) Foundation for Health and Policy and the Breast Cancer Research Foundation (BCRF). It is also part of the education and outreach for the IU Engineered nanoBIO Node and the NCI-funded cancer systems biology grant U01CA232137. The model is built using PhysiCell (version 1.6.1): a C++ framework for multicellular systems biology.

First, you need to compile the PhysiCell model for calibration, on PhysiCell_model folder
```
# your compiler needs to support OpenMP
$ make
```

Then, you can calibrate the model using python script
```
# script using python 3, it need of numpy library
$ python CalibScript.py
```