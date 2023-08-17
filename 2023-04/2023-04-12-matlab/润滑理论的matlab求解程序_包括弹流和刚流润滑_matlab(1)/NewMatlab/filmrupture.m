function [Hr,Hi]=filmrupture(P)  %±¾º¯ÊıµÄ¹¦ÄÜÊÇÓÍÄ¤ÆÆÁÑÎ»ÖÃ£¬¶¼ÊÇÒÔÖáÏò¶Ô³ÆÃæ´¦µÄÊı¾İÎª×¼

[m,n]=size(P);    
for i=1:m        %´ËforÑ­»·ÊÇÇó½âÓÍÄ¤ÆÆÁÑÇøÎ»ÖÃ
    for j=1:n
      if(P(i,j)==0)
        Hr=i;
        Hi=j;
      break;
end
end
end