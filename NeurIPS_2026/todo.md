TODO List pour rendre moins chatgptesque :
 - remplacer les e.g
 - remplacer les -- et ---
 - éviter les formules du type : "X: Y..."
 - éviter les redondances, formulations alambiqués
 
 
 Confs pertinentes en IA

 NeurIPS, ICLR, ICML, CVPR, ICCV/ECCV, ACL, EMNLP, WACV, COLM, CoLLAs, RLC, AISTATS, KDD, IJCAI, AAAI, UAI, COLT, CHIL, MLHC, TMLR, JMLR, FAccT, CHI, Nature Machine Intelligence

A baseline is a point in 6 dimensions space
 - D1 (world model backbone): no WM, 
 - D2 ...
 - D3
 - D4
 - D5
 - D6

For each baseline, we compute some metrics
 - cumulated reward over some testing episodes in "single-variant mode", "known-variants", "unknown-variants"
 - standard-deviation over some testing episodes in "single-variant mode", "known-variants", "unknown-variants"
 - learning rate as the number of steps required to achieve a sufficient cumulative reward threshold and lower a sufficient standard-deviation
 - learning resources cost
 - ... TODO

In the appendix, all of the baselines need to be displayed in results-displaying figures such as graph, tables, curves. For each baseline:
 - For C1 (Improved long-horizon fidelity)
    - among existing other curves, we must display the compound error curve to measure the out-of-band at different horizons from small to big
    - among other floatting-point in the t-SNE representing the reconstructed joint-observation and real joint-observation, we must also display the floatting points for reconstructed and real joint-observations (if the baseline does include a WM, else we simply don't display)
 - For C2 (Improved construction efficiency)
    - among existing other curves, we must display the cost (in time, measured complexity, RAM, CPU, etc.)
 - For C3 (Improved downstream performance)
    - among existing other curves, we must display the learning curve
    - among existing values in the reward table, we must display the average of cumulated reward over several episodes with the plus-or-minus
 - For C4 (Robustness to environment variations)
    - among existing values in the robustness table, we must display the cumulated reward and standard-deviation from several episodes in the single-variant mode (we collect episodes by testing with the same environment variant), known-variants (we collect episodes by playing a different environment variant each time considering those environment variants were all already used during training), unknown-variants (we collect episodes by playing a different variant at each time considering those environment variants are new and were not used during training). The last mode is supposed to show robust trained agents are.
    - among existing values in the WM robustness table, we change the kappa value and run the training to see what happens