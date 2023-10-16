from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from .forms import MonteCarloForm
from django.shortcuts import render, redirect
from django.urls import reverse
import os
from django.http import HttpResponse


def monte_carlo_simulator(request):
    if request.method == "POST":
        form = MonteCarloForm(request.POST)
        if form.is_valid():
            home_dir = os.path.expanduser("~")
            save_dir = os.path.join(home_dir, "Downloads")
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)
            filename = "probability_graph.pdf"
            full_path = os.path.join(save_dir, filename)

            sim_quantity = form.cleaned_data["sim_quantity"]
            min_val = form.cleaned_data["min_val"]
            max_val = form.cleaned_data["max_val"]
            target_val = form.cleaned_data["target_val"]

            sim_result = np.random.uniform(min_val, max_val, sim_quantity)

            plt.figure()
            plt.hist(sim_result, density=True, edgecolor="white")
            plt.axvline(target_val, color="r")
            plt.savefig(full_path, format="pdf")

            with open(full_path, "rb") as f:
                response = HttpResponse(f.read(), content_type="pdf")
                response[
                    "Content-Disposition"
                ] = 'attachment; filename="probability_graph.pdf"'
                return response

            probability = (sim_result > target_val).sum() / sim_quantity

            return render(
                request,
                "projects/monte_carlo_simulator.html",
                {"probability": probability},
            )
    else:
        form = MonteCarloForm()
    return render(
        request, "projects/monte_carlo_simulator.html", context={"form": form}
    )
