
                                         TRANSACTION CONTROL LANGUAGE(VIDEO 19,20,21)


TRANSACTION TO PERFORM ANY OPERATION ON TABLE LIKE
            
			   INSERTING
			   UPDATING
			   DELEATING

THE ABOVE OPERATION ARE USED TO CONTROL DATA IN TABLE

==> TO CONTROL THE DATA OF THE TABLE PURPOSE
    
	     BEGIN TRANSACTION
		 COMMIT
		 ROLLBACK
		 SAVEPOINT

CREATE TABLE BRANCH(BCODE INT, BNAME VARCHAR(50),LOCATION VARCHAR(20))

TESTING

INSERT INTO BRANCH(BCODE,BNAME,LOCATION) VALUES(101,'HDFC','GZP')

UPDATE BRANCH SET LOCATION='GZB'

DELETE FROM  BRANCH WHERE LOCATION='GZB'

BEGIN TRANSACTION
ROLLBACK

SELECT*FROM BRANCH

THESE THREE OPERATION (UPDATE INSERT DELETE) ARE AUTUCOMMIT (THIS WORK EXECUTED PERMANENTLY BY SYSTEM)IN SQL SERVER 

TO REMOVE UPPER PROBLEM IN EXPLICIT TRANSACTION MODE THEN WE PERFORM ROLLBACK OPERATION 


BEGIN ==>TO START THE TRANSACTION 

COMMIT==> TO MAKE TRANSACTIN IS PERMANENT EXPLICITELY(BY USER)
      ==> ONCE THE OPERATION IS COMMIT THEN WE CANNOT ROLLBACK

ROLLBACK ===> ROLLBACK IS NOTHING BUT CANCEL TRANSACTION IT WORK SIMILAR TO UNDO BUTTON
       SYNTAX
	          BEGIN TRANSACTION
	          ROLLBACK

EX1:
BEGIN TRANSACTION
INSERT INTO BRANCH VALUES(1021,'HDFC','GZP')
COMMIT

BEGIN TRANSACTION
ROLLBACK

BEGIN TRANSACTION
UPDATE BRANCH SET LOCATION='DELHI' WHERE BCODE=1021
COMMIT

BEGIN TRANSACTION
DELETE FROM BRANCH WHERE BCODE=1021
COMMIT


BEGIN TRANSACTION
ROLLBACK

SELECT*FROM BRANCH

BEGIN TRANSACTION
DELETE FROM BRANCH WHERE BCODE=1021
DELETE FROM BRANCH WHERE BCODE=1022
DELETE FROM BRANCH WHERE BCODE=1023
COMMIT  =============================> IF WE USE COMMIT THEN NO CHANCE TO GAIN DATA AGAIN AFTER DELETING MEANS WE NOT GAIN TRANSATION AGAIN

BEGIN TRANSACTION    
ROLLBACK

SELECT*FROM BRANCH

SAVEPOINT ==>  IT IS USED TO CREATE TEMPORARY MEMORY FOR STORE THE VALUES WHICH WE WANT TO  CONDITIONALLY CANCELED(NOTHING BUT ROLLBACK) 

SELECT*FROM BRANCH

BEGIN TRANSACTION
DELETE FROM BRANCH WHERE BCODE=1021  -----------> BOTH DATA PUT IN BUFFER BECAUSE IT IS NOT COMMITED 
DELETE FROM BRANCH WHERE BCODE=1022  
SAVE TRANSACTION S1----------------------------> STORE DATA IN POINTER
DELETE FROM BRANCH WHERE BCODE=1023


BEGIN TRANSACTION
ROLLBACK TRANSACTION S1

BEGIN TRANSACTION
ROLLBACK         --------------> IT RETURN ONLY DATA WHICH PUT IN BUFFER

SELECT*FROM BRANCH