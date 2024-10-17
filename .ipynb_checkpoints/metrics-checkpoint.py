{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8171376b-ab20-4897-9414-62df1db8e758",
   "metadata": {
    "editable": true,
    "slideshow": {
     "slide_type": ""
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "from sys import float_info\n",
    "\n",
    "def estimate_roc(discriminant_score, labels):\n",
    "    # Count the number of samples in each class\n",
    "    N_labels = np.array((sum(labels == 0), sum(labels == 1)))\n",
    "    \n",
    "    # Sort scores to determine threshold probabilities\n",
    "    sorted_score = sorted(discriminant_score)\n",
    "    \n",
    "    # Use gamma values to account for all classification splits\n",
    "    gammas = np.concatenate([[sorted_score[0] - float_info.epsilon], sorted_score, [sorted_score[-1] + float_info.epsilon]])\n",
    "    \n",
    "    # Calculate decision labels for each observation for each gamma\n",
    "    decisions = [discriminant_score >= g for g in gammas]\n",
    "    \n",
    "    # Retrieve indices where false positives and true positives occur\n",
    "    ind10 = [np.argwhere((d == 1) & (labels == 0)) for d in decisions]\n",
    "    ind11 = [np.argwhere((d == 1) & (labels == 1)) for d in decisions]\n",
    "    \n",
    "    # Compute false positive rates (FPR) and true positive rates (TPR)\n",
    "    p10 = [len(inds) / N_labels[0] for inds in ind10]\n",
    "    p11 = [len(inds) / N_labels[1] for inds in ind11]\n",
    "    \n",
    "    # Return ROC data with FPR on x-axis and TPR on y-axis\n",
    "    roc = {}\n",
    "    roc['p10'] = np.array(p10)\n",
    "    roc['p11'] = np.array(p11)\n",
    "    \n",
    "    return roc, gammas\n",
    "\n",
    "def get_binary_classification_metrics(predictions, labels):\n",
    "    # Count the number of samples in each class\n",
    "    N_labels = np.array((sum(labels == 0), sum(labels == 1)))\n",
    "    \n",
    "    # Get indices of true negatives, false positives, false negatives, true positives\n",
    "    ind_00 = np.where((predictions == 0) & (labels == 0))[0]\n",
    "    ind_10 = np.where((predictions == 1) & (labels == 0))[0]\n",
    "    ind_01 = np.where((predictions == 0) & (labels == 1))[0]\n",
    "    ind_11 = np.where((predictions == 1) & (labels == 1))[0]\n",
    "    \n",
    "    # Compute classification metrics: TNR, FPR, FNR, TPR\n",
    "    class_metrics = {\n",
    "        'TNR': len(ind_00) / N_labels[0],\n",
    "        'FPR': len(ind_10) / N_labels[0],\n",
    "        'FNR': len(ind_01) / N_labels[1],\n",
    "        'TPR': len(ind_11) / N_labels[1]\n",
    "    }\n",
    "    \n",
    "    return class_metrics"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
