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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.models.error_class import ErrorClass
from typing import Optional, Set
from typing_extensions import Self

class BackupGenericStats(BaseModel):
    """
    Specifies the stats which are generic for all adapters.
    """ # noqa: E501
    data_ingested: Optional[StrictInt] = Field(default=None, description="Specifies the amount of data which has been ingested in bytes.", alias="dataIngested")
    data_ingestion_rate: Optional[StrictInt] = Field(default=None, description="Specifies the rate at which data is being ingested in bytes per minute.", alias="dataIngestionRate")
    error_classes: Optional[List[ErrorClass]] = Field(default=None, description="Divides the errors into classes for better understanding for the user.", alias="errorClasses")
    estimated_backup_time: Optional[StrictInt] = Field(default=None, description="Specifies the time in which backup should finish in minutes.", alias="estimatedBackupTime")
    num_errors: Optional[StrictInt] = Field(default=None, description="Specifies the number of errors for this run.", alias="numErrors")
    remaining_data_ingested: Optional[StrictInt] = Field(default=None, description="Specifies the amount of data which has to be ingested in bytes.", alias="remainingDataIngested")
    __properties: ClassVar[List[str]] = ["dataIngested", "dataIngestionRate", "errorClasses", "estimatedBackupTime", "numErrors", "remainingDataIngested"]

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
        """Create an instance of BackupGenericStats from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in error_classes (list)
        _items = []
        if self.error_classes:
            for _item_error_classes in self.error_classes:
                if _item_error_classes:
                    _items.append(_item_error_classes.to_dict())
            _dict['errorClasses'] = _items
        # set to None if data_ingested (nullable) is None
        # and model_fields_set contains the field
        if self.data_ingested is None and "data_ingested" in self.model_fields_set:
            _dict['dataIngested'] = None

        # set to None if data_ingestion_rate (nullable) is None
        # and model_fields_set contains the field
        if self.data_ingestion_rate is None and "data_ingestion_rate" in self.model_fields_set:
            _dict['dataIngestionRate'] = None

        # set to None if error_classes (nullable) is None
        # and model_fields_set contains the field
        if self.error_classes is None and "error_classes" in self.model_fields_set:
            _dict['errorClasses'] = None

        # set to None if estimated_backup_time (nullable) is None
        # and model_fields_set contains the field
        if self.estimated_backup_time is None and "estimated_backup_time" in self.model_fields_set:
            _dict['estimatedBackupTime'] = None

        # set to None if num_errors (nullable) is None
        # and model_fields_set contains the field
        if self.num_errors is None and "num_errors" in self.model_fields_set:
            _dict['numErrors'] = None

        # set to None if remaining_data_ingested (nullable) is None
        # and model_fields_set contains the field
        if self.remaining_data_ingested is None and "remaining_data_ingested" in self.model_fields_set:
            _dict['remainingDataIngested'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BackupGenericStats from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dataIngested": obj.get("dataIngested"),
            "dataIngestionRate": obj.get("dataIngestionRate"),
            "errorClasses": [ErrorClass.from_dict(_item) for _item in obj["errorClasses"]] if obj.get("errorClasses") is not None else None,
            "estimatedBackupTime": obj.get("estimatedBackupTime"),
            "numErrors": obj.get("numErrors"),
            "remainingDataIngested": obj.get("remainingDataIngested")
        })
        return _obj


