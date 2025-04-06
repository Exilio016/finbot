# RuleGroupUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**order** | **int** |  | [optional] 
**active** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.rule_group_update import RuleGroupUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of RuleGroupUpdate from a JSON string
rule_group_update_instance = RuleGroupUpdate.from_json(json)
# print the JSON string representation of the object
print(RuleGroupUpdate.to_json())

# convert the object into a dict
rule_group_update_dict = rule_group_update_instance.to_dict()
# create an instance of RuleGroupUpdate from a dict
rule_group_update_from_dict = RuleGroupUpdate.from_dict(rule_group_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


