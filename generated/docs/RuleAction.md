# RuleAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**type** | [**RuleActionKeyword**](RuleActionKeyword.md) |  | 
**value** | **str** | The accompanying value the action will set, change or update. Can be empty, but for some types this value is mandatory. | 
**order** | **int** | Order of the action | [optional] 
**active** | **bool** | If the action is active. Defaults to true. | [optional] [default to True]
**stop_processing** | **bool** | When true, other actions will not be fired after this action has fired. Defaults to false. | [optional] [default to False]

## Example

```python
from openapi_client.models.rule_action import RuleAction

# TODO update the JSON string below
json = "{}"
# create an instance of RuleAction from a JSON string
rule_action_instance = RuleAction.from_json(json)
# print the JSON string representation of the object
print(RuleAction.to_json())

# convert the object into a dict
rule_action_dict = rule_action_instance.to_dict()
# create an instance of RuleAction from a dict
rule_action_from_dict = RuleAction.from_dict(rule_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


