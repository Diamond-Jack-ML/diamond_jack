WITH CommentRank AS (
  SELECT        
    c.issue_id,        
    c.created AS comment_created,        
    FORMAT(            
      'Issue Comment %d\nCreated On : %s\nCreated By : %s (%s)\n%s\n%s\n%s\n',            
      ROW_NUMBER() OVER(PARTITION BY c.issue_id ORDER BY c.created),            
      CAST(c.created AS VARCHAR),            
      u.name,            
      u.email,            
      '-------------------------',            
      c.body,            
      '-------------------------'        
    ) AS formatted_comment    
  FROM        
    jira.comment c    
  JOIN        
    jira.user u ON c.author_id = u.id
)
SELECT    
  i.id as issue_id,    
  i.summary as issue_summary,    
  i.created as issue_created,    
  FORMAT(        
    '\nIssue ID : %d\nCreated On : %s\nSummary : %s\nStatus : %s\nPriority : %s\n\n%s',        
    i.id,        
    CAST(i.created AS VARCHAR),        
    i.summary,        
    i.status,        
    i.priority,        
    LISTAGG(cr.formatted_comment, '\n') WITHIN GROUP (ORDER BY cr.comment_created)    
  ) AS issue_details
FROM    
  jira.issue i
LEFT JOIN    
  CommentRank cr ON i.id = cr.issue_id
GROUP BY    
  i.id, i.summary, i.created, i.status, i.priority;
