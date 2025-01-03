if __name__ == "__main__":
    from datetime import datetime
    from api import GlobalSense
    import time
    import pandas as pd
    import numpy as np
    import fetchdata

    time_program_start = time.time()

    MINUTES_FINDING_DATA = 8

    TOTAL_ITERATIONS = 60*MINUTES_FINDING_DATA
    MS_BREAK = 1000
    
    global_sense = GlobalSense()
    
    for i in range(TOTAL_ITERATIONS+1):
        time_start = time.time()
        global_sense.run_tests()
        time.sleep(MS_BREAK/1000 - (time.time() - time_start))

        # global_sense.results[12].append(time.time()-time_start)

    print(f"data collection took: {time.time() - time_program_start} seconds, estimated {MINUTES_FINDING_DATA*60}")

    print(global_sense.results)
    global_sense.results = [x[10::] for x in global_sense.results]
    new_results = np.rot90(global_sense.results)

    df = pd.DataFrame(data=reversed(new_results), columns=global_sense.result_labels)
    df.to_csv("../data/results.csv")
    
    print(np.average(np.average(fetchdata.fetchProcessed()[0])))