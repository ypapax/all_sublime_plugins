module.exports = (autocb)=>

	await rf.getO "telsAll", defer telsObjectList
	telIdList = []
	for tel in telsObjectList
		counterO tel, telsObjectList
		await insertTel tel, defer()
		telIdList.push tel.Id

	return [null, telIdList]	