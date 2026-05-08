# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!
Projects = AutodeskAPIClient(
    aps_client_id= APS_CLIENT_ID,
    aps_client_secret= APS_CLIENT_SECRET,
    ssa_oxygen_id= SSA_OXYGEN_ID,
    key_id= KEY_ID,
    private_key= PRIVATE_KEY,
    ## account_id=ACCOUNT_ID,
    scope= SCOPE  # optional, defaults to projects if omitted
)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
