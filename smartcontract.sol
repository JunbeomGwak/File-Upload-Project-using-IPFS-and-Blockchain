pragma solidity ^0.8.0;
pragma experimental ABIEncoderV2;
contract Owner {
    address public fileowner;
    
    /* 발신자의 address을 fileowner에 저장*/
    constructor() public{
        fileowner = msg.sender;
    }
    /* modifier은 함수의 동작을 변경시키기 위해 사용 */
    /* _는 함수의 실행시점 -> 코드 추가시 _을 기준으로 작성*/
    /* require은 인자의 값이 false이면 즉시 함수 실행을 중단하고 모든 상태 변환을 되돌림*/
    modifier onlyOwner {
        require(msg.sender == fileowner); // check if fileowner same msg.sender
        _;
    }
    /* transferOwnership함수가 실행되면 onlyOwner함수가 실행되고 만약 require(false)이면 즉시 중단 */
    /* 아니면 새로운 owner을 fileowner로 바꾼다 */
    function transferOwnership(address newOwner) public onlyOwner { // if this function call, 
        fileowner = newOwner; // owner changed
    }
    
    /* 리턴 타입을 address(이더리움 주소)로 리턴 */
    function getOwner() public view returns (address) { // return fileowner(type: address)
        return fileowner;
    }
}

contract StorefileHash is Owner {
    struct File {
        string filename;
        uint UploadDate;
        uint Filesize;
    }

    struct CopyrightStruct {
        string Artist;
        string Createdtime; // When this file created
        string Type; // File Type ex) music, video, photo etc
        string Description; // Simple Description of file
        string timestamp;
        string owner;
        string ipfs_hash;
    }
    
        
    mapping(string => File) private files; // string : key, File : Value
    mapping(string => string[]) private fileOwners;
    string[] public owners;
    uint public ownerID = 0;
    CopyrightStruct[] public copyright; // dynamic size 
    uint index;
    
    event FileUpload(string ownername, string filehash, File file);
    event Copyright(string Artist, string Createdtime, string Type, string Description, string timestamp, string owner, string ipfs_hash);

    function fileupload(string memory _ownername, string memory _filehash, string memory _filename, uint _filesize) onlyOwner public{
        ownerID++;
        owners.push(_ownername);
        File memory f = File(_filename, block.timestamp, _filesize); // now = block.timestamp
        files[_filehash] = f;
        emit FileUpload(_ownername, _filehash, f);
    }

    function Exsistcheck(string memory _filehash) onlyOwner public view returns (bool) {
        if(files[_filehash].Filesize > 0) {
            return true;
        }
        return false;
    }
    
    function getOwnerName() onlyOwner public view returns (address) {
        return fileowner;
    }
    
    function getfileinfo(string memory _filehash) onlyOwner public view returns (string memory, uint, uint) {
        return (files[_filehash].filename, files[_filehash].UploadDate, files[_filehash].Filesize);
    }

    function addCopyright(string memory _Artist, 
                    string memory _Createdtime, 
                    string memory  _Type,
                    string memory _Description, 
                    string memory _timestamp, 
                    string memory _owner, 
                    string memory _ipfshash) public {
        copyright.push(CopyrightStruct(_Artist, _Createdtime, _Type, _Description, _timestamp, _owner, _ipfshash));
        index++;
        emit Copyright(_Artist, _Createdtime, _Type, _Description, _timestamp, _owner, _ipfshash);
    }
    
    function getCopyright(uint _idx) public view returns(string memory, string memory, string memory, string memory) {
        return (copyright[_idx].Artist, copyright[_idx].Createdtime, copyright[_idx].Type, copyright[_idx].Description);
    }
}
