# COT Positioning Analysis

Python analysis of extreme Commitments of Traders (COT) positioning signals in Euro FX, Crude Oil, and E-mini S&P 500 futures.

**Key Insights**:
- Strongest edges in Crude Oil (+2.2–2.3% average 1-week returns after extremes)
- Clean contrarian signals in Euro FX
- Near-perfect spec-hedger mirroring in Euro (-0.991) and Oil (-0.984)

![Main Results](results\cot_positioning_extremes_comparison.png)

## Methodology 
- Z-scores computed on commercial and non-commercial net positions
- Extremes filtered at ±2 standard deviations
- Average forward returns calculated at 1-week 2-week and 4-week horizons
- Comparison of commercial (hedgers) vs non-commercial (speculators)

## How to Run
1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/cot-positioning-analysis.git
2. install dependecies:
   ```bash
   pip install pandas matplotlib seaborn
3. Run analysis
4. ```bash
   open cot_positioning_analysis.ipynb
   
[Idowu praise]     
git: @praise-west   
Linkedin: https://www.linkedin.com/in/praise-idowu-1025ab342?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BPmoiWebxS%2FWAo88ZGcQeTA%3D%3D