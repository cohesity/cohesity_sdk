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
from cohesity_sdk.helios.models.aws_postgres_metadata import AwsPostgresMetadata
from typing import Optional, Set
from typing_extensions import Self

class AwsPostgresEntityMetadata(BaseModel):
    """
    Specifies the entity metadata of aws postgres entities.
    """ # noqa: E501
    db_engine_id: Optional[StrictStr] = Field(default=None, description="Specifies the engine id of the database which can be used to identify the type of database.", alias="dbEngineId")
    metadata_list: List[AwsPostgresMetadata] = Field(description="Specifies the metadata list.", alias="metadataList")
    __properties: ClassVar[List[str]] = ["dbEngineId", "metadataList"]

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
        """Create an instance of AwsPostgresEntityMetadata from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in metadata_list (list)
        _items = []
        if self.metadata_list:
            for _item_metadata_list in self.metadata_list:
                if _item_metadata_list:
                    _items.append(_item_metadata_list.to_dict())
            _dict['metadataList'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AwsPostgresEntityMetadata from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dbEngineId": obj.get("dbEngineId"),
            "metadataList": [AwsPostgresMetadata.from_dict(_item) for _item in obj["metadataList"]] if obj.get("metadataList") is not None else None
        })
        return _obj


