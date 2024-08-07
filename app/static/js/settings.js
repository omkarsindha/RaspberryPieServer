function changeIP(){
    const ipAddress = document.getElementById('ip-address').value;
    const subnetMask = document.getElementById('subnet-mask').value;
    const defaultGateway = document.getElementById('default-gateway').value;

    const confirmation = confirm(`IP Address: ${ipAddress}\nSubnet Mask: ${subnetMask}\nDefault Gateway: ${defaultGateway}\nAre you sure you want to change the IP? You will be able to access switcher at new IP after change.`);

    if (confirmation) {
        fetch('/changeIP', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                ipAddress: ipAddress,
                subnetMask: subnetMask,
                defaultGateway: defaultGateway
            })
        })
        .then(response => response.json())
        .then(data => {
            alert('Settings updated successfully!');
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred while updating the settings.');
        });
    }
};
