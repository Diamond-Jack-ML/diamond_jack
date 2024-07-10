WITH CommentRank AS (
  SELECT        
    c.page_id,        
    c.created AS comment_created,        
    FORMAT(            
      'Page Comment %d\nCreated On : %s\nCreated By : %s (%s)\n%s\n%s\n%s\n',            
      ROW_NUMBER() OVER(PARTITION BY c.page_id ORDER BY c.created),            
      CAST(c.created AS VARCHAR),            
      u.name,            
      u.email,            
      '-------------------------',            
      c.body,            
      '-------------------------'        
    ) AS formatted_comment    
  FROM        
    confluence.comment c    
  JOIN        
    confluence.user u ON c.author_id = u.id
)
SELECT    
  p.id as page_id,    
  p.title as page_title,    
  p.created as page_created,    
  FORMAT(        
    '\nPage ID : %d\nCreated On : %s\nTitle : %s\n\n%s',        
    p.id,        
    CAST(p.created AS VARCHAR),        
    p.title,        
    LISTAGG(cr.formatted_comment, '\n') WITHIN GROUP (ORDER BY cr.comment_created)    
  ) AS page_details
FROM    
  confluence.page p
LEFT JOIN    
  CommentRank cr ON p.id = cr.page_id
GROUP BY    
  p.id, p.title, p.created;
