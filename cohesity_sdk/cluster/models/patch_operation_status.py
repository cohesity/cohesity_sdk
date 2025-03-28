# coding: utf-8

"""
    Cohesity REST API

    Cohesity API provides a RESTful interface to access the various data management operations on Cohesity cluster and Helios.

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.cluster.models.service_unit_progress import ServiceUnitProgress
from typing import Set
from typing_extensions import Self

class PatchOperationStatus(BaseModel):
    """
    Specifies the status of the current or the last patch operation.
    """ # noqa: E501
    in_progress: Optional[StrictBool] = Field(default=None, description="Specifies whether a operation is in progress now.", alias="inProgress")
    operation: Optional[StrictStr] = Field(default=None, description="Specifies the patch operation. It is either apply or revert patch operation.")
    operation_message: Optional[StrictStr] = Field(default=None, description="Specifies a message about the patch operation.", alias="operationMessage")
    percentage: Optional[StrictInt] = Field(default=None, description="Specifies the percentage of completion of the current patch operation in progress or the last patch operation completed.")
    services_progress: Optional[List[ServiceUnitProgress]] = Field(default=None, description="Specifies the details of patch operation services at each patch level.", alias="servicesProgress")
    time_remaining_seconds: Optional[StrictInt] = Field(default=None, description="Specifies the time remaining to complete the patch operation.", alias="timeRemainingSeconds")
    time_taken_seconds: Optional[StrictInt] = Field(default=None, description="Specifies the time taken so far to complete the patch operation.", alias="timeTakenSeconds")
    __properties: ClassVar[List[str]] = ["inProgress", "operation", "operationMessage", "percentage", "servicesProgress", "timeRemainingSeconds", "timeTakenSeconds"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of PatchOperationStatus from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in services_progress (list)
        _items = []
        if self.services_progress:
            for _item_services_progress in self.services_progress:
                if _item_services_progress:
                    _items.append(_item_services_progress.to_dict())
            _dict['servicesProgress'] = _items
        # set to None if in_progress (nullable) is None
        # and model_fields_set contains the field
        if self.in_progress is None and "in_progress" in self.model_fields_set:
            _dict['inProgress'] = None

        # set to None if operation (nullable) is None
        # and model_fields_set contains the field
        if self.operation is None and "operation" in self.model_fields_set:
            _dict['operation'] = None

        # set to None if operation_message (nullable) is None
        # and model_fields_set contains the field
        if self.operation_message is None and "operation_message" in self.model_fields_set:
            _dict['operationMessage'] = None

        # set to None if percentage (nullable) is None
        # and model_fields_set contains the field
        if self.percentage is None and "percentage" in self.model_fields_set:
            _dict['percentage'] = None

        # set to None if services_progress (nullable) is None
        # and model_fields_set contains the field
        if self.services_progress is None and "services_progress" in self.model_fields_set:
            _dict['servicesProgress'] = None

        # set to None if time_remaining_seconds (nullable) is None
        # and model_fields_set contains the field
        if self.time_remaining_seconds is None and "time_remaining_seconds" in self.model_fields_set:
            _dict['timeRemainingSeconds'] = None

        # set to None if time_taken_seconds (nullable) is None
        # and model_fields_set contains the field
        if self.time_taken_seconds is None and "time_taken_seconds" in self.model_fields_set:
            _dict['timeTakenSeconds'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PatchOperationStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "inProgress": obj.get("inProgress"),
            "operation": obj.get("operation"),
            "operationMessage": obj.get("operationMessage"),
            "percentage": obj.get("percentage"),
            "servicesProgress": [ServiceUnitProgress.from_dict(_item) for _item in obj["servicesProgress"]] if obj.get("servicesProgress") is not None else None,
            "timeRemainingSeconds": obj.get("timeRemainingSeconds"),
            "timeTakenSeconds": obj.get("timeTakenSeconds")
        })
        return _obj


