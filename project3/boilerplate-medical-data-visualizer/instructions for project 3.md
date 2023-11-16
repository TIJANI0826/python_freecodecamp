
### Data description
The rows in the dataset represent patients and the columns represent information like body measurements, results from various blood tests, and lifestyle choices. You will use the dataset to explore the relationship between cardiac disease, body measurements, blood markers, and lifestyle choices.

File name: <mark>medical_examination.csv</mark>

|Feature | Variable Type | Variable | Value Type
|------------ | ---------- | --------- | ---------- |
| Age | Objective Feature | <mark>age</mark> | int (days) |
| Height | Objective Feature | <mark>height</mark> | int (cm) |
| Weight | Objective Feature | <mark>weight</mark> | float (kg) |
| Gender | Objective Feature | <mark>gender</mark> | categorical code |
| Systolic blood pressure | Examination Feature | <mark>ap_hi</mark> | int |
| Diastolic blood pressure | Examination Feature | <mark>ap_lo</mark> | int |
| Cholesterol | Examination Feature | <mark>cholesterol</mark> | 1: normal, 2: above normal, 3: well above normal |
| Glucose | Examination Feature | <mark>gluc</mark> | 1: normal, 2: above normal, 3: well above normal |
| Smoking | Subjective Feature | <mark>smoke</mark> | binary |
| Alcohol intake | Subjective Feature | <mark>alco</mark> | binary | 
| Physical activity | Subjective Feacture | <mark>active</mark> | binary |
| Presence or absence of cardiovascular disease | Target Variable | <mark>cardio</mark> | binary |

### Tasks
Create a chart similar to <mark>examples/Figure_1.png</mark>, where we show the counts of good and bad outcomes for the <mark>cholesterol</mark>, <mark>gluc</mark>, <mark>alco</mark>, <mark>active</mark>, and <mark>smoke</mark> variables for patients with cardio=1 and cardio=0 in different panels.

Use the data to complete the following tasks in <mark>medical_data_visualizer.py</mark>:

- Add an <mark>overweight</mark> column to the data. To determine if a person is overweight, first calculate their BMI by dividing their weight in kilograms by the square of their height in meters. If that value is > 25 then the person is overweight. Use the value 0 for NOT overweight and the value 1 for overweight.
- Normalize the data by making 0 always good and 1 always bad. If the value of <mark>cholesterol</mark> or <mark>gluc</mark> is 1, make the value 0. If the value is more than 1, make the value 1.
- Convert the data into long format and create a chart that shows the value counts of the categorical features using seaborn's <mark>catplot()</mark> . The dataset should be split by 'Cardio' so there is one chart for each <mark>cardio</mark> value. The chart should look like <mark>examples/Figure_1.png</mark>.
- Clean the data. Filter out the following patient segments that represent incorrect data:  
    - diastolic pressure is higher than systolic (Keep the correct data with <mark>(df['ap_lo'] <= df['ap_hi'])</mark>)
    - diastolic pressure is higher than systolic (Keep the correct data with <mark>(df['ap_lo'] <= df['ap_hi'])</mark>
    - height is less than the 2.5th percentile (Keep the correct data with <mark>(df['height'] >= df['height'].quantile(0.025))</mark>)
    - height is more than the 97.5th percentile
    - weight is less than the 2.5th percentile
    - weight is more than the 97.5th percentile
- Create a correlation matrix using the dataset. Plot the correlation matrix using seaborn's <mark>heatmap()</mark>. Mask the upper triangle. The chart should look like <mark>examples/Figure_2.png</mark>.
Any time a variable is set to <mark>None</mark>, make sure to set it to the correct code.

Unit tests are written for you under <mark>test_module.py</mark>.

### Development
For development, you can use <mark>main.py</mark> to test your functions. Click the "run" button and <mark>main.py</mark> will run.

### Testing
We imported the tests from <mark>test_module.py</mark> to <mark>main.py</mark> for your convenience. The tests will run automatically whenever you hit the "run" button.

### Submitting
Copy your project's URL and submit it to freeCodeCamp.