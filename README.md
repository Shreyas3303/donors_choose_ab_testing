# DonorsChoose Text Length A/B Testing

> Figuring out if making teachers write longer project descriptions actually helps get their projects approved

## What is this project about?

I was looking at DonorsChoose data and noticed something interesting - projects that got approved tended to have longer descriptions than ones that got rejected. Approved projects had essays around 1,015 characters while rejected ones were only about 962 characters.

This got me thinking: **what if we made teachers write longer descriptions? Would that actually help more projects get approved?**

That's what this A/B test is trying to figure out.

## What the project does

This is basically a simulation(since I dont have means of carrying out an actual experiment) to see what would happen if DonorsChoose required teachers to write longer project descriptions. Here's what it does:

1. **Looks at the current data** - 109,248 projects, about 85% get approved
2. **Simulates different scenarios** - what if we required 800, 1000, or 1200 character minimums?
3. **Sees what happens** - do more projects get approved? Do fewer? What's the financial impact?

## The test groups

- **Group A (Control)**: Keep things how they are now (no minimum length)
- **Group B**: Require at least 800 characters
- **Group C**: Require at least 1000 characters  
- **Group D**: Require at least 1200 characters

## How to run it

```bash
# Install the stuff you need
pip install pandas numpy matplotlib seaborn scipy

# Run the analysis
python text_length_ab_test.py
```

Or if you want to play around with it in a notebook:
```bash
jupyter notebook text_length_ab_test.ipynb
```

## What you'll see

The script will show you:
- Charts comparing approved vs rejected projects by text length
- How each test group performs compared to the control
- Statistical tests to see if the differences are real or just random
- Business Impact

## The results

Spoiler: The results were actually surprising. Making teachers write longer descriptions actually **reduced** approval rates instead of improving them. Results:

- **Control group**: 84.86% approval rate
- **800 character minimum**: 82.45% approval rate (worse!)
- **1000 character minimum**: 81.23% approval rate (even worse!)
- **1200 character minimum**: 79.87% approval rate (much worse!)

## Files in this project

- `text_length_ab_test.py` - The main script that runs everything
- `text_length_ab_test.ipynb` - Same thing but in a Jupyter notebook
- `donors_choose_eda.ipynb` - My original exploration of the data
- `get_data.py` - Script to get the data
- `donors_choose_data.csv` - The actual dataset (it's big - 126MB)