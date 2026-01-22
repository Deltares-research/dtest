import os
import sys
from pathlib import Path

import pandas as pd
from pandas import DataFrame
from pandas.testing import assert_frame_equal


def compare_two_df(output_df: DataFrame | Path, ref_df: DataFrame | Path):
    if isinstance(output_df, Path):
        output_df = pd.read_csv(output_df)

    if isinstance(ref_df, Path):
        ref_df = pd.read_csv(ref_df)

    # output_df has a different order in linux than in windows, so sort before comparing
    output_df_sorted = output_df.sort_values(by=list(output_df.columns)).reset_index(
        drop=True
    )
    ref_df_sorted = ref_df.sort_values(by=list(ref_df.columns)).reset_index(drop=True)

    assert_frame_equal(
        output_df_sorted, ref_df_sorted, rtol=1e-3, atol=1e-8, check_dtype=False
    )
