# RuleTrigger


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**type** | [**RuleTriggerKeyword**](RuleTriggerKeyword.md) |  | 
**value** | **str** | The accompanying value the trigger responds to. This value is often mandatory, but this depends on the trigger. | 
**prohibited** | **bool** | If &#39;prohibited&#39; is true, this rule trigger will be negated. &#39;Description is&#39; will become &#39;Description is NOT&#39; etc. | [optional] [default to False]
**order** | **int** | Order of the trigger | [optional] [readonly] 
**active** | **bool** | If the trigger is active. Defaults to true. | [optional] [default to True]
**stop_processing** | **bool** | When true, other triggers will not be checked if this trigger was triggered. Defaults to false. | [optional] [default to False]

## Example

```python
from openapi_client.models.rule_trigger import RuleTrigger

# TODO update the JSON string below
json = "{}"
# create an instance of RuleTrigger from a JSON string
rule_trigger_instance = RuleTrigger.from_json(json)
# print the JSON string representation of the object
print(RuleTrigger.to_json())

# convert the object into a dict
rule_trigger_dict = rule_trigger_instance.to_dict()
# create an instance of RuleTrigger from a dict
rule_trigger_from_dict = RuleTrigger.from_dict(rule_trigger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


