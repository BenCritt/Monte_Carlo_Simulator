# This is the form for the Monte Carlo Simulator.
class MonteCarloForm(forms.Form):
    # Integer field for the number of simulations to run.
    sim_quantity = forms.IntegerField(
        label="Number of Simulations ",
        # Validators to ensure the number of simulations is within an acceptable range.
        validators=[
            MinValueValidator(
                1, message="The number of simulations must be at least 1."
            ),
            MaxValueValidator(
                1000000,
                message="The number of simulations cannot exceed 1,000,000.  This limit ensures server resources aren't overused.",
            ),
        ],
    )
    # Floating point fields for the minimum and maximum values for the simulation.
    min_val = forms.FloatField(label="Minimum Value")
    max_val = forms.FloatField(label="Maximum Value")
    # Floating point field for the target value in the simulation.
    target_val = forms.FloatField(label="Target Value")
    # Optional integer field for the number of simulations for a second data range.
    second_sim_quantity = forms.IntegerField(
        required=False,
        label="Second Number of Simulations",
        validators=[
            MinValueValidator(
                1,
                message="The value for second number of simulations, if you wish to include a second data range, must be at least 1.  If you only want one data range in your graph, please leave the secondary fields blank.",
            ),
            MaxValueValidator(
                1000000,
                message="The number of second simulations cannot exceed 1,000,000.  This limit ensures server resources aren't overused.",
            ),
        ],
    )
    # Optional floating point fields for the minimum and maximum values for the second data range.
    second_min_val = forms.FloatField(label="Second Minimum Value", required=False)
    second_max_val = forms.FloatField(label="Second Maximum Value", required=False)
    # Optional floating point field for the target value for the second data range.
    second_target_val = forms.FloatField(label="Second Target Value", required=False)
