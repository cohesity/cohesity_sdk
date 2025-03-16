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
from typing_extensions import Annotated
from cohesity_sdk.cluster.models.mongo_db_cdp_job_info import MongoDBCdpJobInfo
from cohesity_sdk.cluster.models.no_sql_protection_group_object_params import NoSqlProtectionGroupObjectParams
from typing import Optional, Set
from typing_extensions import Self

class MongoDBProtectionGroupParams(BaseModel):
    """
    Specifies the parameters for MongoDB Protection Group.
    """ # noqa: E501
    auto_scale_concurrency: Optional[StrictBool] = Field(default=None, description="Specifies the flag to automatically scale number of concurrent IO Streams that will be created to exchange data with the cluster.", alias="autoScaleConcurrency")
    bandwidth_mbps: Optional[StrictInt] = Field(default=None, description="Specifies the maximum network bandwidth that each concurrent IO Stream can use for exchanging data with the cluster.", alias="bandwidthMBPS")
    concurrency: Optional[StrictInt] = Field(default=None, description="Specifies the maximum number of concurrent IO Streams that will be created to exchange data with the cluster.")
    custom_source_name: Optional[StrictStr] = Field(default=None, description="The user specified name for the Source on which this protection was run.", alias="customSourceName")
    exclude_object_ids: Optional[List[StrictInt]] = Field(default=None, description="Specifies the objects to be excluded in the Protection Group.", alias="excludeObjectIds")
    objects: Optional[Annotated[List[NoSqlProtectionGroupObjectParams], Field(min_length=1)]] = Field(default=None, description="Specifies the objects to be included in the Protection Group.")
    source_id: Optional[StrictInt] = Field(default=None, description="Object ID of the Source on which this protection was run .", alias="sourceId")
    source_name: Optional[StrictStr] = Field(default=None, description="Specifies the name of the Source on which this protection was run.", alias="sourceName")
    cdp_info: Optional[MongoDBCdpJobInfo] = Field(default=None, alias="cdpInfo")
    __properties: ClassVar[List[str]] = ["autoScaleConcurrency", "bandwidthMBPS", "concurrency", "customSourceName", "excludeObjectIds", "objects", "sourceId", "sourceName", "cdpInfo"]

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
        """Create an instance of MongoDBProtectionGroupParams from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "custom_source_name",
            "source_id",
            "source_name",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in objects (list)
        _items = []
        if self.objects:
            for _item_objects in self.objects:
                if _item_objects:
                    _items.append(_item_objects.to_dict())
            _dict['objects'] = _items
        # override the default output from pydantic by calling `to_dict()` of cdp_info
        if self.cdp_info:
            _dict['cdpInfo'] = self.cdp_info.to_dict()
        # set to None if auto_scale_concurrency (nullable) is None
        # and model_fields_set contains the field
        if self.auto_scale_concurrency is None and "auto_scale_concurrency" in self.model_fields_set:
            _dict['autoScaleConcurrency'] = None

        # set to None if bandwidth_mbps (nullable) is None
        # and model_fields_set contains the field
        if self.bandwidth_mbps is None and "bandwidth_mbps" in self.model_fields_set:
            _dict['bandwidthMBPS'] = None

        # set to None if concurrency (nullable) is None
        # and model_fields_set contains the field
        if self.concurrency is None and "concurrency" in self.model_fields_set:
            _dict['concurrency'] = None

        # set to None if custom_source_name (nullable) is None
        # and model_fields_set contains the field
        if self.custom_source_name is None and "custom_source_name" in self.model_fields_set:
            _dict['customSourceName'] = None

        # set to None if exclude_object_ids (nullable) is None
        # and model_fields_set contains the field
        if self.exclude_object_ids is None and "exclude_object_ids" in self.model_fields_set:
            _dict['excludeObjectIds'] = None

        # set to None if source_id (nullable) is None
        # and model_fields_set contains the field
        if self.source_id is None and "source_id" in self.model_fields_set:
            _dict['sourceId'] = None

        # set to None if source_name (nullable) is None
        # and model_fields_set contains the field
        if self.source_name is None and "source_name" in self.model_fields_set:
            _dict['sourceName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MongoDBProtectionGroupParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "autoScaleConcurrency": obj.get("autoScaleConcurrency"),
            "bandwidthMBPS": obj.get("bandwidthMBPS"),
            "concurrency": obj.get("concurrency"),
            "customSourceName": obj.get("customSourceName"),
            "excludeObjectIds": obj.get("excludeObjectIds"),
            "objects": [NoSqlProtectionGroupObjectParams.from_dict(_item) for _item in obj["objects"]] if obj.get("objects") is not None else None,
            "sourceId": obj.get("sourceId"),
            "sourceName": obj.get("sourceName"),
            "cdpInfo": MongoDBCdpJobInfo.from_dict(obj["cdpInfo"]) if obj.get("cdpInfo") is not None else None
        })
        return _obj


