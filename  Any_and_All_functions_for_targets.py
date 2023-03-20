
attempts_for_each_target = [
  [True, False, True],  # Постріли у першу мішень
  [False, False, True],  # Постріли у другу мішень
  [False, True],  # Постріли у третю мішень
 ]

def all_targets_hit(attempts_for_each_target: list) -> bool:
    # write your code here
    for i in range(len(attempts_for_each_target)):
        if any(attempts_for_each_target[i]) == False:
            return False
    return True

print(all_targets_hit(attempts_for_each_target))

##############################
###### Mentor resolution #####
##############################

def all_targets_hit(attempts_for_each_target: list) -> bool:
    targets_results = []
    for current_target_attempts in attempts_for_each_target:
        targets_results.append(any(current_target_attempts))
    return all(targets_results)