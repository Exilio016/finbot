# RuleRead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Immutable value | 
**id** | **str** |  | 
**attributes** | [**Rule**](Rule.md) |  | 
**links** | [**ObjectLink**](ObjectLink.md) |  | 

## Example

```python
from openapi_client.models.rule_read import RuleRead

# TODO update the JSON string below
json = "{}"
# create an instance of RuleRead from a JSON string
rule_read_instance = RuleRead.from_json(json)
# print the JSON string representation of the object
print(RuleRead.to_json())

# convert the object into a dict
rule_read_dict = rule_read_instance.to_dict()
# create an instance of RuleRead from a dict
rule_read_from_dict = RuleRead.from_dict(rule_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


