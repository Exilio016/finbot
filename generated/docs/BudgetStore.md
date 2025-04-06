# BudgetStore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**active** | **bool** |  | [optional] 
**order** | **int** |  | [optional] [readonly] 
**notes** | **str** |  | [optional] 
**auto_budget_type** | [**AutoBudgetType**](AutoBudgetType.md) |  | [optional] 
**auto_budget_currency_id** | **str** | Use either currency_id or currency_code. Defaults to the user&#39;s default currency. | [optional] 
**auto_budget_currency_code** | **str** | Use either currency_id or currency_code. Defaults to the user&#39;s default currency. | [optional] 
**auto_budget_amount** | **str** |  | [optional] 
**auto_budget_period** | [**AutoBudgetPeriod**](AutoBudgetPeriod.md) |  | [optional] 

## Example

```python
from openapi_client.models.budget_store import BudgetStore

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetStore from a JSON string
budget_store_instance = BudgetStore.from_json(json)
# print the JSON string representation of the object
print(BudgetStore.to_json())

# convert the object into a dict
budget_store_dict = budget_store_instance.to_dict()
# create an instance of BudgetStore from a dict
budget_store_from_dict = BudgetStore.from_dict(budget_store_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


