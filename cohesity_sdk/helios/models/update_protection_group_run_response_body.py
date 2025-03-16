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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.helios.models.failed_run_details import FailedRunDetails
from typing import Optional, Set
from typing_extensions import Self

class UpdateProtectionGroupRunResponseBody(BaseModel):
    """
    Specifies the response of update Protection Group Runs request.
    """ # noqa: E501
    failed_runs: Optional[List[FailedRunDetails]] = Field(default=None, description="Specifies a list of ids of Protection Group Runs that failed to update along with error details.", alias="failedRuns")
    successful_run_ids: Optional[List[StrictStr]] = Field(default=None, description="Specifies a list of ids of Protection Group Runs that are successfully updated.", alias="successfulRunIds")
    __properties: ClassVar[List[str]] = ["failedRuns", "successfulRunIds"]

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
        """Create an instance of UpdateProtectionGroupRunResponseBody from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in failed_runs (list)
        _items = []
        if self.failed_runs:
            for _item_failed_runs in self.failed_runs:
                if _item_failed_runs:
                    _items.append(_item_failed_runs.to_dict())
            _dict['failedRuns'] = _items
        # set to None if failed_runs (nullable) is None
        # and model_fields_set contains the field
        if self.failed_runs is None and "failed_runs" in self.model_fields_set:
            _dict['failedRuns'] = None

        # set to None if successful_run_ids (nullable) is None
        # and model_fields_set contains the field
        if self.successful_run_ids is None and "successful_run_ids" in self.model_fields_set:
            _dict['successfulRunIds'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpdateProtectionGroupRunResponseBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "failedRuns": [FailedRunDetails.from_dict(_item) for _item in obj["failedRuns"]] if obj.get("failedRuns") is not None else None,
            "successfulRunIds": obj.get("successfulRunIds")
        })
        return _obj


