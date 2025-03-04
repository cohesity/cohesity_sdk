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
from cohesity_sdk.models.datastore_params import DatastoreParams
from typing import Optional, Set
from typing_extensions import Self

class ThrottlingParams(BaseModel):
    """
    Specifies throttling params.
    """ # noqa: E501
    active_task_latency_threshold_msecs: Optional[StrictInt] = Field(default=None, description="If the latency of a datastore is above this value, then an existing backup task that uses the datastore will start getting throttled.", alias="activeTaskLatencyThresholdMsecs")
    data_store_params: Optional[List[DatastoreParams]] = Field(default=None, description="Specifies datastore specific parameters.", alias="dataStoreParams")
    max_concurrent_streams: Optional[StrictInt] = Field(default=None, description="If this value is > 0 and the number of streams concurrently active on a datastore is equal to it, then any further requests to access the datastore would be denied until the number of active streams reduces. This applies for all the datastores in the specified host.", alias="maxConcurrentStreams")
    new_task_latency_threshold_msecs: Optional[StrictInt] = Field(default=None, description="If the latency of a datastore is above this value, then a new backup task that uses the datastore won't be started.", alias="newTaskLatencyThresholdMsecs")
    __properties: ClassVar[List[str]] = ["activeTaskLatencyThresholdMsecs", "dataStoreParams", "maxConcurrentStreams", "newTaskLatencyThresholdMsecs"]

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
        """Create an instance of ThrottlingParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in data_store_params (list)
        _items = []
        if self.data_store_params:
            for _item_data_store_params in self.data_store_params:
                if _item_data_store_params:
                    _items.append(_item_data_store_params.to_dict())
            _dict['dataStoreParams'] = _items
        # set to None if active_task_latency_threshold_msecs (nullable) is None
        # and model_fields_set contains the field
        if self.active_task_latency_threshold_msecs is None and "active_task_latency_threshold_msecs" in self.model_fields_set:
            _dict['activeTaskLatencyThresholdMsecs'] = None

        # set to None if data_store_params (nullable) is None
        # and model_fields_set contains the field
        if self.data_store_params is None and "data_store_params" in self.model_fields_set:
            _dict['dataStoreParams'] = None

        # set to None if max_concurrent_streams (nullable) is None
        # and model_fields_set contains the field
        if self.max_concurrent_streams is None and "max_concurrent_streams" in self.model_fields_set:
            _dict['maxConcurrentStreams'] = None

        # set to None if new_task_latency_threshold_msecs (nullable) is None
        # and model_fields_set contains the field
        if self.new_task_latency_threshold_msecs is None and "new_task_latency_threshold_msecs" in self.model_fields_set:
            _dict['newTaskLatencyThresholdMsecs'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ThrottlingParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "activeTaskLatencyThresholdMsecs": obj.get("activeTaskLatencyThresholdMsecs"),
            "dataStoreParams": [DatastoreParams.from_dict(_item) for _item in obj["dataStoreParams"]] if obj.get("dataStoreParams") is not None else None,
            "maxConcurrentStreams": obj.get("maxConcurrentStreams"),
            "newTaskLatencyThresholdMsecs": obj.get("newTaskLatencyThresholdMsecs")
        })
        return _obj


