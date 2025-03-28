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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Set
from typing_extensions import Self

class QoS(BaseModel):
    """
    Specifies the Quality of Service (QoS) Policy for the View.
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="Specifies the name of the QoS Policy. If not specified, the default is 'BackupTargetLow'.  BackupTargetAuto: (Applicable only for C6K Platform) Use this policy for workloads such as backups, which keep many I/Os outstanding. This policy splits I/Os across SSDs and HDDs to achieve maximum performance based on the current usage. The priority for processing workload with this policy is the same as Backup Target High and Backup Target SSD.  JournaledSequentialDump: Use this policy for workloads that write large amounts of data sequentially to a very small number of files and do not keep many I/Os outstanding. By default data is written to the SSD and has the highest priority and low latency.  TestAndDevHigh: Use this policy for workloads that require lower I/O latency or do not keep many I/Os outstanding, as the I/Os are given higher priority compared to other QoS policies. Data is written to the SSD.  TestAndDevLow: The same as TestAndDev High, except that the I/Os with this QoS policy are given lower priority compared to I/Os with TestAndDev High when there is contention.  BackupTargetCommvault: Use this policy to intelligently detect and exclude application-specific markers to achieve better deduplication when CommVault backup application is writing to a Cohesity View. Data is written to SSD and has the same priority and latency as TestAndDev High.  BackupTargetSSD: Use this policy for workloads such as backups, which keep many I/Os outstanding, but in this case, DataPlatform sends both sequential and random I/Os to SSD. The latency is lower than other Backup Target policies. The priority for processing workload with this policy is the same as Backup Target Auto.  BackupTargetHigh: Use this policy for non-latency sensitive workloads such as backups, which keep many I/Os outstanding. Data is written to HDD and has higher latency compared to other QoS policies writing to a SSD The priority for processing workload with this policy is the same as Backup Target Auto.  BackupTargetLow: The same as Backup Target High, except that the priority for processing workloads with this policy is lower than workloads with Backup Target Auto / High /SSD when there is contention.")
    principal_id: Optional[StrictInt] = Field(default=None, description="Specifies the id of the QoS Policy used for the View. (Deprecated) This parameter is deprecated and shall not be supported in future releases. Use name instead.", alias="principalId")
    principal_name: Optional[StrictStr] = Field(default=None, description="Specifies the name of the QoS Policy. If not specified, the default is 'Backup Target Low'. (To be deprecated in future release, use name instead)", alias="principalName")
    __properties: ClassVar[List[str]] = ["name", "principalId", "principalName"]

    @field_validator('name')
    def name_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['BackupTargetHigh', 'BackupTargetLow', 'TestAndDevHigh', 'TestAndDevLow', 'BackupTargetSSD', 'BackupTargetCommvault', 'JournaledSequentialDump', 'BackupTargetAuto']):
            raise ValueError("must be one of enum values ('BackupTargetHigh', 'BackupTargetLow', 'TestAndDevHigh', 'TestAndDevLow', 'BackupTargetSSD', 'BackupTargetCommvault', 'JournaledSequentialDump', 'BackupTargetAuto')")
        return value

    @field_validator('principal_name')
    def principal_name_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Backup Target High', 'Backup Target Low', 'TestAndDev High', 'TestAndDev Low', 'Backup Target SSD', 'Backup Target Commvault', 'Journaled Sequential Dump', 'Backup Target Auto']):
            raise ValueError("must be one of enum values ('Backup Target High', 'Backup Target Low', 'TestAndDev High', 'TestAndDev Low', 'Backup Target SSD', 'Backup Target Commvault', 'Journaled Sequential Dump', 'Backup Target Auto')")
        return value

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
        """Create an instance of QoS from a JSON string"""
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
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if principal_id (nullable) is None
        # and model_fields_set contains the field
        if self.principal_id is None and "principal_id" in self.model_fields_set:
            _dict['principalId'] = None

        # set to None if principal_name (nullable) is None
        # and model_fields_set contains the field
        if self.principal_name is None and "principal_name" in self.model_fields_set:
            _dict['principalName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of QoS from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "principalId": obj.get("principalId"),
            "principalName": obj.get("principalName")
        })
        return _obj


