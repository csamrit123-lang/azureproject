import dlt

exceptations={
    "rule_1" : "user_id is not null"
}

@dlt.table
@dlt.expect_all_or_drop(exceptations)
def dimuser_stg():
    df=spark.readStream.table("spotify_cata.silver.dimuser")
    return df

dlt.create_streaming_table(
    
    name="dimuser",
    expect_all_or_drop=exceptations
    
    )

dlt.create_auto_cdc_flow(
  target = "dimuser",
  source = "dimuser_stg",
  keys = ["user_id"],
  sequence_by = "updated_at",
  stored_as_scd_type = 2,
  track_history_except_column_list = None,
  name = None,
  once = False
)