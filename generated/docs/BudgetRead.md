# BudgetRead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Immutable value | 
**id** | **str** |  | 
**attributes** | [**Budget**](Budget.md) |  | 

## Example

```python
from openapi_client.models.budget_read import BudgetRead

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetRead from a JSON string
budget_read_instance = BudgetRead.from_json(json)
# print the JSON string representation of the object
print(BudgetRead.to_json())

# convert the object into a dict
budget_read_dict = budget_read_instance.to_dict()
# create an instance of BudgetRead from a dict
budget_read_from_dict = BudgetRead.from_dict(budget_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


