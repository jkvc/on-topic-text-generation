import pandas as pd
import os
import numpy as np

WITH_PROMPT = False
MODEL_PREFIX = 'bert_gpt_dau'
POOL_TYPE = 'max'
FILENAME = f'{"with_prompt" if WITH_PROMPT else "without_prompt"}.csv'
FILEPATH = os.path.join(
    '../outputs', MODEL_PREFIX+'_'+POOL_TYPE, FILENAME
)


if __name__ == "__main__":
    df_max = pd.read_csv(FILEPATH)

    try:
        while True:
            idx = np.random.randint(0, len(df_max) + 1)
            print(f'[{idx}]')

            print(f'[highlight]')
            print(df_max.iloc[idx].highlight)

            print(f'[max]')
            print(df_max.iloc[idx].generated)

            input()

    except KeyboardInterrupt:
        pass
