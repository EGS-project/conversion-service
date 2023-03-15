<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">

  <xs:element name="image">
    <xs:complexType>
      <xs:sequence>
        <xs:element name="filename" type="xs:string"/>
        <xs:element name="b64_string" type="xs:string"/>
        <xs:element name="width" type="xs:integer"/>
        <xs:element name="height" type="xs:integer"/>
        <xs:element name="mode" type="xs:string"/>
        <xs:element name="format" type="xs:string"/> 
      </xs:sequence>
    </xs:complexType>
  </xs:element>

</xs:schema>
