import sys
import pandas as pd

old_file = sys.argv[1]
new_file = sys.argv[2]

old_df = pd.read_csv(old_file) if old_file else pd.DataFrame()
new_df = pd.read_csv(new_file)

if not old_df.empty:
    old_df = old_df.set_index("teamId")
    new_df = new_df.set_index("teamId")

    rank_changes = []
    for team_id, row in new_df.iterrows():
        if team_id in old_df.index:
            old_rank = old_df.index.get_loc(team_id) + 1
            new_rank = new_df.index.get_loc(team_id) + 1
            if new_rank < old_rank:
                rank_changes.append(f"🏆 [{row['teamName']}] {old_rank} → {new_rank}🎉")

    if rank_changes:
        print("\n".join(rank_changes))
